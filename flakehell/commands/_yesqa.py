from pathlib import Path
# from .._constants import ExitCodes
from .._logic import YesQA
from .._types import CommandResult


def get_paths(paths):
    for path in paths:
        if path.is_dir():
            yield from get_paths(path.iterdir())
            continue
        if path.suffix != '.py':
            continue
        if not path.is_file():
            continue
        yield path


def yesqa_command(argv) -> CommandResult:
    """Show all installed plugins, their codes prefix, and matched rules from config.
    """
    paths = get_paths(Path(fname) for fname in argv)
    fixer = YesQA()
    for path in paths:
        modified = fixer(path=path)
        if modified:
            print(str(path))
    return 0, ''