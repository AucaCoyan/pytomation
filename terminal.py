import datetime


def is_working_day(date: datetime.date) -> bool:
    if date.weekday() < 5:
        return True
    else:
        return False


def main():
    return "hello"


if __name__ == "__main__":
    now = datetime.date.today()
    print(is_working_day(now))
