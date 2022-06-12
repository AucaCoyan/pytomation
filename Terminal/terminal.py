# -*- coding:utf-8 -*-
import datetime
import subprocess

import psutil


def is_working_day(date: datetime.date, force: bool = False) -> bool:
    if force:
        return True
    elif date.weekday() < 5:
        return True
    else:
        return False


def check_if_terminal_is_open() -> bool:
    proc_list = []
    for proc in psutil.process_iter(["pid", "name"]):
        proc_list.append(proc.info)
        # print(proc.info['name'])
        if proc.info["name"] == "WindowsTerminal.exe":
            print(f"Found it! the process is {proc.info}")
            return True

    print("Windows Terminal is closed")
    return False


def open_terminal() -> None:
    subprocess.Popen(
        args=r"C:\Program Files\WindowsApps\Microsoft.WindowsTerminal_1.13.11431.0_x64__8wekyb3d8bbwe\wt.exe",
        encoding="utf8",
    )


def main(force: bool = False):
    now = datetime.date.today()
    # print(f'Today is working day? {is_working_day(now)}')
    if is_working_day(now, force=force):
        if check_if_terminal_is_open():
            print("Windows Terminal is already open")
        else:
            open_terminal()
        print("is working day!")
    else:
        print("is a weekend day, take some rest!")


if __name__ == "__main__":
    exit(main())
