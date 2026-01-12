import re

LOG_PATTERN = re.compile(
    r"(?P<date>\d{4}-\d{2}-\d{2}) "
    r"(?P<time>\d{2}:\d{2}:\d{2}) "
    r"(?P<level>[A-Z]+) "
    r"(?P<message>.*)"
)


def parse_logs(line: str) -> dict:
    match = LOG_PATTERN.match(line)

    if not match:
        raise ValueError(f"Invalid log format: {line}")
    return match.groupdict()


try:
    with open("logs.txt", "r") as file:
        for line in file:
            print(parse_logs(line))
except FileNotFoundError:
    print("this file doesn't exist")
