from config.aliases import ALIASES


def resolve_alias(command):

    command = command.strip().lower()

    if command in ALIASES:
        return ALIASES[command]

    return command