from services.app_scanner import (
    scan_start_menu,
    launch_app
)

apps = scan_start_menu()

launch_app(
    "visual studio code",
    apps
)