import argparse

from pythongettext.msgfmt import Msgfmt, PoSyntaxError


def check_syntax(filename):
    with open(filename, "rb") as po_file:
        try:
            Msgfmt(po_file, filename).getAsFile()
        except PoSyntaxError as err:
            print(err.msg)
            return 1
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to check.")
    args = parser.parse_args(argv)
    retval = 0
    for filename in args.filenames:
        if check_syntax(filename):
            retval = 1
    return retval


if __name__ == "__main__":
    raise SystemExit(main())
