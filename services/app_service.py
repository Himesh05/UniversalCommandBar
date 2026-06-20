from services.app_scanner import scan_start_menu

APPS = scan_start_menu()


def get_apps():
    return APPS


def get_app_names():
    return list(APPS.keys())

def launch_app(app_name):

    app_name = app_name.lower()

    if app_name in APPS:
        import os

        os.startfile(APPS[app_name])
        return True

    return False