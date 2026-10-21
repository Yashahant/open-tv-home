# Build from source

Use Python 3.9+, JDK 17 or newer, and Android SDK command-line tools. Install `platforms;android-34` and `build-tools;34.0.0` using SDK Manager. No Gradle, Python packages, or proprietary libraries are required.

Set `JAVA_HOME` to the JDK and `ANDROID_HOME` to the SDK. Run from the repository:

```text
python build.py
```

On systems where Python is called `python3`, use that name instead. The script supports Windows tool suffixes and Unix paths. You can override SDK versions using `ANDROID_API` and `BUILD_TOOLS_VERSION`; those versions must already be installed and support the app's APIs.

The output is `out/open-tv-home.apk`. The script compiles Java, creates DEX, packages and aligns entries, signs, and verifies the APK. It does not connect to a TV or change any device settings.

## Signing

The first local build creates `.signing/development.jks`, an ignored development key with the conventional development password `android`. Keep it to update your own test installation. Do not publish the key or use it for a maintained public release.

For a release, supply `KEYSTORE` (path to an existing private keystore) and `KEYSTORE_PASS` via your private environment/CI secret store. Keys must remain outside the repository. Keep the same release key for future updates. Do not put signing passwords in command examples, issue reports, or source control.

The application ID stays `com.ansub.tvhome` for source continuity with the upstream project. Independently signed builds conflict with an installed upstream or other fork build. Follow the setup guide's signature-mismatch recovery instructions.

## Tool failures

If `aapt2` crashes, check your JDK and Android SDK versions, then try reinstalling the official SDK build tools. Build failures must be resolved before installing the APK.

## Tests before publishing

1. Build from a clean checkout and verify the signature.
2. Inspect APK contents and confirm only required application files are included.
3. Install on a supported test TV and verify Home, Back, D-pad navigation, Settings, wallpapers, apps, and Inputs.
4. Verify default startup stays on Home; separately test optional startup input after a real reboot.
5. Check devices without inputs or without a media app; check graceful failure if a saved app is removed.
6. Verify recovery to stock Home before experimenting with firmware-specific defaults.

Physical testing on one model cannot establish universal compatibility. Record the model/API level and untested behavior in release notes.


