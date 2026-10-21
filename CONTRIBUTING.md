# Contributing

Keep changes small and describe the observable problem, resulting behavior, and tests. Build with `python build.py`. Test D-pad navigation, Home/Back, wallpaper selection, app-list refresh, Inputs, and unavailable-app behavior. Startup-input changes need a real reboot test on a supported TV.

Do not introduce automatic package disabling, hidden service-menu changes, automatic network scans, or embedded device addresses. Preserve the MIT licence and upstream attribution. Avoid telemetry or network dependencies in the launcher.

Never commit signing keys, passwords, device logs, photographs, generated APKs, or account information. Submit compatibility reports with personal details removed. Unsupported vendor behavior should fail gracefully with manual controls available.

