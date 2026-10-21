# Setup, developer mode, and recovery

## What you need

- An Android TV or Google TV, a remote, and a computer.
- Android SDK Platform Tools (`adb`) from [Google](https://developer.android.com/tools/releases/platform-tools).
- A built APK. Build requirements are in [BUILD.md](BUILD.md).
- For wireless connection, both devices on the same trusted local network. Internet is not required for local ADB after tools are installed.

## Enable developer options

Open the TV's About page. Common paths are **Settings > System > About** or **Settings > Device Preferences > About**. If Device Preferences is absent, look for System or About directly. Find **Build**, **Build number**, or **Android TV OS build**, and press OK seven times. A developer confirmation should appear. Return to Settings and find Developer options.

Enable the debugging method your TV provides: USB debugging / ADB debugging, Network debugging, or Wireless debugging. Do not enable OEM unlocking; this setup does not require rooting or unlocking the bootloader. Names and availability vary by manufacturer. [Android developer-options reference](https://developer.android.com/studio/debug/dev-options).

## Connect the computer

Replace placeholders below with the values on YOUR TV. Do not paste the angle brackets literally.

**Wireless debugging with pairing:** if the TV exposes a pairing screen, use its pairing address and code, then its separate connection address:

```text
adb pair <TV_IP>:<PAIRING_PORT>
adb connect <TV_IP>:<CONNECTION_PORT>
adb devices
```

Pairing and connection ports can differ. Do not assume port 5555 for paired wireless debugging. [Official connection guide](https://developer.android.com/studio/run/device).

**Older / vendor network ADB:** some TVs offer a network-debugging switch and listen on a displayed port, often 5555. Use the port documented by your TV:

```text
adb connect <TV_IP>:<ADB_PORT>
adb devices
```

USB debugging alone does NOT guarantee network ADB. Older devices may require an initial supported USB debugging connection and `adb tcpip 5555`; many TV USB ports are host-only and cannot provide that connection. Do not use an unsuitable USB-A-to-A cable. Follow your manufacturer's supported connection method. [ADB reference](https://developer.android.com/tools/adb).

Accept the debugging authorization on the TV only for your own trusted computer. If unauthorized, check the TV prompt. If offline or timed out, verify the current IP, debugging setting, network isolation, and connection port. Always check `adb devices` before running commands; do not leave commands waiting indefinitely for an absent TV.

## Inspect and install

Use `-s <SERIAL>` when more than one device is connected. For network ADB, the serial is normally the address and port shown by `adb devices`.

```text
adb -s <SERIAL> shell getprop ro.product.model
adb -s <SERIAL> shell getprop ro.build.version.sdk
adb -s <SERIAL> shell cmd package resolve-activity --brief -a android.intent.action.MAIN -c android.intent.category.HOME
adb -s <SERIAL> install -r out/open-tv-home.apk
adb -s <SERIAL> shell am start -n com.ansub.tvhome/.MainActivity
```

Save the original Home component locally for recovery. First test this launcher without changing the default. On older Android versions some `cmd package` commands may be unavailable; use the TV's Home-app chooser/settings where offered.

If installation reports `INSTALL_FAILED_UPDATE_INCOMPATIBLE`, an app with this package ID has a different signature. Use an update from the same signing identity, or deliberately uninstall the conflicting app only after selecting a working alternative Home. Uninstalling removes its app settings. Never automatically remove it just to silence the error.

## Select Home

Prefer the TV's **Default apps > Home app** screen or a chooser shown after pressing Home. Some supported devices also accept:

```text
adb -s <SERIAL> shell cmd package set-home-activity --user 0 com.ansub.tvhome/.MainActivity
```

Press Home and verify what actually opens. A command reporting Success is not sufficient: manufacturers may still force their own Home. Do not disable stock packages by default. If this firmware blocks replacement, keep using the launcher manually while investigating that model.

## Customize

- **Settings > Wallpaper:** built-in gradients.
- **Settings > Add app to home:** pin an installed app. Hold OK on its tile to manage it.
- **All apps:** open apps without pinning them.
- **Inputs:** select inputs registered by the TV. Disconnected ports may still be listed; a TV box may list none.
- **Settings > Media browser app:** choose an installed TV-compatible file/media app. The USB shortcut remembers it. If you choose the wrong app, choose again here.
- **Settings > Startup input:** choose Stay on Home or an input for the NEXT boot. It waits for boot completion and input registration. Boot launches depend on manufacturer policy.

Plug a pendrive into a compatible USB port, open Inputs > USB, and browse it in your chosen app. Storage support and permissions are managed by that app and Android.

## Recovery

Select the original Home app through settings or use its saved component:

```text
adb -s <SERIAL> shell cmd package set-home-activity --user 0 <ORIGINAL_HOME_COMPONENT>
adb -s <SERIAL> shell input keyevent KEYCODE_HOME
```

Verify it opens before uninstalling Open TV Home. If YOU previously disabled a stock package, restore that exact package with `adb shell pm enable <PACKAGE>`; do not use a guessed list. Disabling stock launchers can also break their input panels or recommendations services.

This project does not change app background restrictions, animation scales, factory menus, or power-on behavior. Those are separate device settings. Do not copy hidden factory-menu changes from another model.

After setup, disable debugging or revoke unneeded debugging authorizations when you no longer need them. Never expose ADB through router port forwarding.

