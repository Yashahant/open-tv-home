"""Dependency-free APK build; requires Python 3.9+, JDK 17+, Android SDK 34."""
import os
from pathlib import Path
import shutil
import struct
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)
sdk_value = os.environ.get('ANDROID_HOME') or os.environ.get('ANDROID_SDK_ROOT')
if not sdk_value:
    raise SystemExit('Set ANDROID_HOME to your Android SDK directory.')
sdk = Path(sdk_value)
tools = sdk / 'build-tools' / os.environ.get('BUILD_TOOLS_VERSION', '34.0.0')
android = sdk / 'platforms' / ('android-' + os.environ.get('ANDROID_API', '34')) / 'android.jar'
if not android.is_file() or not tools.is_dir():
    raise SystemExit('Install platforms;android-34 and build-tools;34.0.0, or set version overrides.')
out = ROOT / 'out'
classes = out / 'classes'
if classes.exists():
    shutil.rmtree(classes) # Fixed generated directory inside this project only.
classes.mkdir(parents=True)
(out / 'dex').mkdir(exist_ok=True)
windows = os.name == 'nt'

def tool(name):
    suffix = ('.bat' if name in ('d8', 'apksigner') else '.exe') if windows else ''
    return str(tools / (name + suffix))

def java(name):
    home = os.environ.get('JAVA_HOME')
    return str(Path(home) / 'bin' / (name + ('.exe' if windows else ''))) if home else name

def run(*args, **kwargs):
    subprocess.run([str(a) for a in args], check=True, **kwargs)

run(tool('aapt2'), 'link', '-o', out / 'base.apk', '-I', android,
    '--manifest', ROOT / 'AndroidManifest.xml', '--min-sdk-version', '21', '--target-sdk-version', '34')
run(java('javac'), '-encoding', 'UTF-8', '-source', '8', '-target', '8',
    '-bootclasspath', str(android) + os.pathsep + str(tools / 'core-lambda-stubs.jar'),
    '-d', classes, *sorted(ROOT.glob('*.java')))
run(tool('d8'), '--min-api', '21', '--release', '--lib', android,
    '--output', out / 'dex', *sorted(classes.rglob('*.class')))

# Store each entry with a 4-byte-aligned data offset, without bundling private assets.
with zipfile.ZipFile(out / 'base.apk') as base, zipfile.ZipFile(out / 'aligned.apk', 'w') as dest:
    entries = [(name, base.read(name)) for name in base.namelist()]
    entries.append(('classes.dex', (out / 'dex' / 'classes.dex').read_bytes()))
    for name, data in entries:
        info = zipfile.ZipInfo(name)
        padding = (-(dest.fp.tell() + 30 + len(name.encode('utf-8')))) % 4
        if padding:
            info.extra = struct.pack('<HH', 0xffff, padding) + b'\0' * padding
        dest.writestr(info, data)
with zipfile.ZipFile(out / 'aligned.apk') as apk, open(out / 'aligned.apk', 'rb') as raw:
    for entry in apk.infolist():
        raw.seek(entry.header_offset + 26)
        name_len, extra_len = struct.unpack('<HH', raw.read(4))
        assert (entry.header_offset + 30 + name_len + extra_len) % 4 == 0

# Release keys are supplied externally. Local development uses a generated ignored key.
key_value = os.environ.get('KEYSTORE')
if key_value:
    key = Path(key_value).resolve()
    if not key.is_file() or not os.environ.get('KEYSTORE_PASS'):
        raise SystemExit('Release signing needs an existing KEYSTORE and KEYSTORE_PASS.')
else:
    key = ROOT / '.signing' / 'development.jks'
    key.parent.mkdir(exist_ok=True)
    os.environ['KEYSTORE_PASS'] = 'android'
    if not key.exists():
        run(java('keytool'), '-genkeypair', '-keystore', key, '-storepass:env', 'KEYSTORE_PASS',
            '-keypass:env', 'KEYSTORE_PASS', '-alias', 'tvhome', '-keyalg', 'RSA',
            '-keysize', '2048', '-validity', '10000', '-dname', 'CN=Open TV Home Development')
run(tool('apksigner'), 'sign', '--ks', key, '--ks-pass', 'env:KEYSTORE_PASS',
    '--out', out / 'open-tv-home.apk', out / 'aligned.apk')
run(tool('apksigner'), 'verify', out / 'open-tv-home.apk')
print('Built and signature-verified: out/open-tv-home.apk')

