import sys
from src.parser import parse_args, run_command
from src.utils import format_output


def main() -> int:
    args = parse_args(sys.argv[1:])
    result = run_command(args)
    print(format_output(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
