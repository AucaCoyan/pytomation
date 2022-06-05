# -*- coding:utf-8 -*-
import datetime
import subprocess
import sys

import psutil


def is_working_day(date: datetime.date) -> bool:
    if date.weekday() < 5:
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
    # subprocess.call([sys.executable, r'C:\Windows apps shorcuts\Windows Terminal - Shortcut.lnk'])
    subprocess.Popen(
        args="C:\\Windows apps shorcuts\\Windows Terminal - Shortcut.lnk",
        encoding="utf8",
    )
    # subprocess.Popen(r'C:\\Windows\\System32\\calc.exe')


def main():
    now = datetime.date.today()
    # print(f'Today is working day? {is_working_day(now)}')
    if is_working_day(now):
        check_if_terminal_is_open()
        open_terminal()
        print("is working day!")
    else:
        print("is a weekend day, take some rest!")


if __name__ == "__main__":
    open_terminal()
    exit()
    exit(main())
