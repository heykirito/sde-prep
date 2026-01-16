import re

class LogEntry:
    def __init__(self, date: str, time: str, level: str, message: str):
        self.date = date
        self.time = time
        self.level = level
        self.message = message

    def __str__(self):
        return f"[{self.date} {self.time} {self.level}: {self.message}]"

class InvalidLogFormat(Exception):
    pass
    
class LogParser:
    log_pattern = re.compile(
        r"(?P<date>\d{4}-\d{2}-\d{2}) "
        r"(?P<time>\d{2}:\d{2}:\d{2}) "
        r"(?P<level>[A-Z]+) "
        r"(?P<message>.*)"
    )

    def parse(self, line: str) -> LogEntry:
        match = self.log_pattern.match(line.strip())

        if not match:
            raise InvalidLogFormat(f"Invaild log line: {line}")
        data = match.groupdict()

        return LogEntry(
            date=data["date"],
            time=data["time"],
            level=data["level"],
            message=data["message"],
        )

class FileReader:
    def __init__(self, path:str):
        self.path=path

    def read_lines(self):
        try:
            with open(self.path, "r") as f:
                for line in f:
                    yield line
        except FileNotFoundError:
            raise FileReader(f"File not found: {self.path}")


def main():
    reader = FileReader("logs.txt")
    parser = LogParser()

    entries = []

    for line in reader.read_lines():
        try:
            entry = parser.parse(line)
            entries.append(entry)
        except InvalidLogFormat as e:
            print("skipping bad line: ", e)

    print("Parsed entries:")
    for e in entries:
        print(e)


if __name__ == "__main__":
    main()
