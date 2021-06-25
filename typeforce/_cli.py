import sys
import typing
from argparse import ArgumentParser
from ._core import Explorer


def main(argv: typing.List[str], stream: typing.TextIO) -> int:
    parser = ArgumentParser()
    parser.add_argument('--exe', default=sys.executable)
    parser.add_argument('--dry', action='store_true')
    args = parser.parse_args(argv)
    explorer = Explorer(exe=args.exe, dry=args.dry)
    for line in explorer.run():
        print(line, file=stream)
    return 0


def entrypoint():
    sys.exit(main(argv=sys.argv[1:], stream=sys.stdout))
