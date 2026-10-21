# Open TV Home

A lightweight, remote-friendly Android TV launcher, derived from [Ansub Khan's TV Detox](https://github.com/Ansub/tv-detox). MIT licensed; original attribution is preserved in [LICENSE](LICENSE).

## Open TV Home vs the default launcher

Default launchers vary by TV brand, model, and software version. This compares common Android TV / Google TV behavior; individual devices may differ.

| Area | Open TV Home | Default TV launcher |
|---|---|---|
| Home screen | Simple clock, app shortcuts, input shortcuts, and gradient wallpapers | Usually includes recommendations, content rows, and manufacturer features |
| Advertising and recommendations | No ads or recommendation feed in the launcher | May show sponsored content and recommendations, depending on device and region |
| Everyday navigation | Direct access to All apps, Inputs, Settings, and network settings | Often provides richer content discovery and service integrations |
| Performance | Avoids animated backgrounds and recommendation feeds; caches app lists and icons | Workload varies with its features and services; may benefit from vendor optimizations |
| Input selection | Lists inputs exposed through Android's TV input APIs | Often has deeper integration with the TV's input labels, CEC devices, and vendor menus |
| USB media | Opens a file/media browser selected by the user | May include a built-in media browser and automatic USB prompts |
| Startup behavior | Optional input launch after boot completion; Home is the default | May offer last-input restoration or manufacturer-specific startup settings |
| Customization | Source code is available under MIT; apps, gradients, and startup input are configurable | Usually configurable through built-in settings; source is generally not available |
| Voice, search, and recommendations | No built-in voice search or personalized recommendations; system assistant behavior depends on the TV | Usually integrates these features more closely |
| Installation and updates | Requires sideloading/building and manual updates; default-Home support varies | Preinstalled and usually updated through the manufacturer or platform |
| Compatibility and support | Limited device testing; community-maintained | Designed for the device and supported through its vendor/platform |

### Strong points

- A straightforward Home screen for people who prefer apps and inputs over content feeds.
- No launcher accounts, analytics, or internet permission.
- Open source: users can inspect, modify, and redistribute it under the MIT licence.
- User-selectable media browser and optional startup input instead of a fixed vendor setup.

### Weak points and trade-offs

- Less content discovery, voice/search integration, and vendor-specific functionality.
- Input switching and startup behavior depend on what the TV firmware allows. Some TVs force their stock Home screen.
- USB browsing needs a separate app; this launcher does not play media itself.
- Manual installation and updates, limited hardware testing, and incomplete translation coverage for newer features.
- No measured evidence yet that it boots faster, uses less memory, or makes every TV more responsive than its default launcher. A simpler interface does not guarantee a faster device.

**Choose Open TV Home** if you want a simple, customizable app-and-input screen. **Keep the default launcher** if you prefer integrated recommendations, voice features, vendor support, and automatic updates.

## Features

- Clock, date, and built-in gradient wallpapers.
- All apps, Inputs, Settings, and network shortcuts.
- Add apps to Home from Settings; hold OK on a home app to manage it.
- Automatically detects the TV inputs exposed by your device.
- USB shortcut opens a file/media browser that **you choose**. The launcher itself does not read USB files.
- Optional startup input, selected in Settings. Default: **stay on Home**.
- Startup selection waits for Android boot completion and input registration. No periodic launch retry loop.
- Cached app list, small on-demand icons, and no wallpaper animation.

## Compatibility

Designed for Android TV and Google TV running Android 5.0 or later (API 21+). Tested on Android TV 10; compatibility with other devices and versions may vary.

TV sticks and boxes usually have HDMI **output**, not selectable HDMI inputs. An empty input list is normal there. Vendor firmware may restrict replacement Home apps, boot launches, Wi-Fi information, or access to TV input players. Samsung Tizen, LG webOS, and Roku are not Android TV and cannot run this APK.

## Start here

1. Read [Setup and developer mode](SETUP.md).
2. Build with `python build.py` using [Build instructions](BUILD.md), or use an APK published by a maintainer you trust.
3. Install and launch without disabling the stock launcher.
4. Test remote navigation, apps, settings, and inputs before choosing it as Home.
5. Optionally choose a media browser and startup input in Settings.

For help from an AI with local terminal access, copy the [Claude / ChatGPT Codex setup prompt](AI-SETUP-PROMPT.md). A normal chat without computer access can guide you but cannot connect to the TV by itself.

## Privacy and permissions

No analytics, accounts, or ads. The launcher does not request internet access. Settings remain in Android's private app preferences. Network-state permissions support the Wi-Fi indicator; boot permission supports optional startup input; uninstall permission allows the system confirmation dialog for app removal. A selected media browser is a separate app with its own permissions and privacy behavior.



## Known limits

- Changing the default Home depends on manufacturer firmware. Keep the stock launcher installed and enabled by default.
- Some stock input menus live inside the stock launcher package. Disabling it can break those menus or related services.
- Startup input makes one automatic attempt per boot. If it fails, use Inputs manually. It does not turn on a TV from mains power or override firmware power settings.
- USB playback support depends on your media browser, TV, file system, and codecs.
- UI additions currently use English text; upstream translations do not cover every new label.
- The app retains the upstream package ID `com.ansub.tvhome`. A differently signed version of that package cannot be updated in place. See the setup guide before removing anything.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md). Report your TV model, Android version, expected behavior, and reproducible steps.

This is an independent derivative, not an official release or endorsement by the upstream author or any TV manufacturer.



