import re

log_patterns = re.compile(
    r"(?P<date>\d{4}-\d{2}-\d{2}) "
    r"(?P<time>\d{2}:\d{2}:\d{2}) "
    r"(?P<level>[A-Z]+) "
    r"(?P<message>.*)"
)


def parse_log(line: str) -> dict:
    match = log_patterns.match(line)

    if not match:
        raise ValueError(f"Log in the correct format: {line}")
    else:
        return match.groupdict()


try:
    with open("logs.txt", "r") as file:
        for line in file:
            print(parse_log(line))
except FIleNotFoundError:
    print("The provided file doesn't exist")


