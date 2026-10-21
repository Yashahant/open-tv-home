# Open TV Home

A lightweight, remote-friendly Android TV launcher, derived from [Ansub Khan's TV Detox](https://github.com/Ansub/tv-detox). MIT licensed; original attribution is preserved in [LICENSE](LICENSE).

## Features

- Clock, date, and built-in gradient wallpapers. No personal photographs are bundled.
- All apps, Inputs, Settings, and network shortcuts.
- Add apps to Home from Settings; hold OK on a home app to manage it.
- Detects the passthrough inputs exposed by the TV, rather than assuming three HDMI ports or an AV port.
- USB shortcut opens a file/media browser that **you choose**. The launcher itself does not read USB files.
- Optional startup input, selected in Settings. Default: **stay on Home**.
- Startup selection waits for Android boot completion and input registration. No periodic launch retry loop.
- Cached app list, small on-demand icons, and no wallpaper animation.

## Compatibility

Designed for Android TV / Google TV with API 21+ (Android 5.0+). This is not a claim of certification or universal hardware testing. The development device runs Android TV 10; other manufacturers and OS versions need testing.

TV sticks and boxes usually have HDMI **output**, not selectable HDMI inputs. An empty input list is normal there. Vendor firmware may restrict replacement Home apps, boot launches, Wi-Fi information, or access to TV input players. Samsung Tizen, LG webOS, and Roku are not Android TV and cannot run this APK.

## Start here

1. Read [Setup and developer mode](SETUP.md).
2. Build with `python build.py` using [Build instructions](BUILD.md), or use an APK published by a maintainer you trust.
3. Install and launch without disabling the stock launcher.
4. Test remote navigation, apps, settings, and inputs before choosing it as Home.
5. Optionally choose a media browser and startup input in Settings.

For help from an AI with local terminal access, copy the [Claude / ChatGPT Codex setup prompt](AI-SETUP-PROMPT.md). A normal chat without computer access can guide you but cannot connect to the TV by itself.

## Privacy and permissions

No analytics, accounts, ads, bundled personal media, or INTERNET permission. Settings remain in Android's private app preferences. Network-state permissions support the Wi-Fi indicator; boot permission supports optional startup input; uninstall permission allows the system confirmation dialog for app removal. A selected media browser is a separate app with its own permissions and privacy behavior.

This source distribution excludes development screenshots, device logs, network addresses, local paths, APK backups, and signing keys. Do not upload your keys or private photos when contributing.

## Known limits

- Changing the default Home depends on manufacturer firmware. Keep the stock launcher installed and enabled by default.
- Some stock input menus live inside the stock launcher package. Disabling it can break those menus or related services.
- Startup input makes one automatic attempt per boot. If it fails, use Inputs manually. It does not turn on a TV from mains power or override firmware power settings.
- USB playback support depends on your media browser, TV, file system, and codecs.
- UI additions currently use English text; upstream translations do not cover every new label.
- The app retains the upstream package ID `com.ansub.tvhome`. A differently signed version of that package cannot be updated in place. See the setup guide before removing anything.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md). Report your TV model, Android version, expected behavior, and reproducible steps. Remove addresses, account names, media filenames, and other personal details from logs or screenshots first.

This is an independent derivative, not an official release or endorsement by the upstream author or any TV manufacturer.

