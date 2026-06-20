import subprocess
import os
from unittest import result
import webbrowser
from commands.calculator_commands import calculate


COMMAND_HANDLERS = {
    "browser": lambda: open_browser(),
    "vscode": lambda: subprocess.Popen("code"),
    "downloads": lambda: open_downloads(),
    "desktop": lambda: open_desktop(),
}


def open_downloads():
    path = os.path.join(os.path.expanduser("~"), "Downloads")

    if os.path.exists(path):
        os.startfile(path)


def open_desktop():
    possible_paths = [
        os.path.join(os.path.expanduser("~"), "Desktop"),
        os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")
    ]

    for path in possible_paths:
        if os.path.exists(path):
            os.startfile(path)
            return

    print("Desktop folder not found.")


def open_browser():
    webbrowser.open("https://www.google.com")


def google_search(query):
    webbrowser.open(
        f"https://www.google.com/search?q={query}"
    )


def youtube_search(query):
    webbrowser.open(
        f"https://www.youtube.com/results?search_query={query}"
    )


def execute_command(command):

    command = command.strip()

    if command.startswith("google "):
        query = command[7:]
        google_search(query)
        return f"Searching Google for: {query}"

    if command.startswith("youtube "):
        query = command[8:]
        youtube_search(query)
        return f"Searching YouTube for: {query}"
    
    result = calculate(command)

    if result is not None:
        return result

    command = command.lower()

    if command in COMMAND_HANDLERS:
        COMMAND_HANDLERS[command]()
        return f"Executed: {command}"

    return f"Unknown command: {command}"