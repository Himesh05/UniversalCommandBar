import os


def scan_start_menu():

    app_paths = {}

    start_menu_locations = [
        os.path.join(
            os.environ["PROGRAMDATA"],
            r"Microsoft\Windows\Start Menu\Programs"
        ),

        os.path.join(
            os.environ["APPDATA"],
            r"Microsoft\Windows\Start Menu\Programs"
        )
    ]

    for location in start_menu_locations:

        if not os.path.exists(location):
            continue

        for root, dirs, files in os.walk(location):

            for file in files:

                if file.endswith(".lnk"):

                    app_name = os.path.splitext(file)[0]

                    app_paths[app_name.lower()] = os.path.join(
                        root,
                        file
                    )

    return app_paths

def launch_app(app_name, apps):

    app_name = app_name.lower()

    if app_name in apps:
        os.startfile(apps[app_name])
        return True

    return False