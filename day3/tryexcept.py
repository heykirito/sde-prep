# Learning try and expect and all that thingy


try:
    x = int("123")
except ValueError:
    print("Conversion Error")
else:
    print("Conversion successfull")
finally:
    print("This always run")


try:
    f = open("./text.txt", "r")
    data = f.read()
except FileNotFoundError:
    print("File not found error")
else:
    print("File read successfully, here's the output")
    print(data)
finally:
    print("Closing file\n")
    f.close()


try:
    y = int("abc")
except ValueError:
    print("Not a number\n")



class InvalidLogFormat(Exception):
    pass


def parse_log(line):
    if "ERROR" not in line:
        raise InvalidLogFormat("Invalid log line")


try:
    parse_log("hello")
except InvalidLogFormat as e:
    print("Bad log", e)
