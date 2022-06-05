import datetime

import pytest

import terminal

testdates = [
    (datetime.datetime(2022, 6, 6), True),  # Monday
    (datetime.datetime(2022, 6, 7), True),
    (datetime.datetime(2022, 6, 8), True),
    (datetime.datetime(2022, 6, 9), True),
    (datetime.datetime(2022, 6, 10), True),
    (datetime.datetime(2022, 6, 11), False),
    (datetime.datetime(2022, 6, 12), False),  # Sunday
]


@pytest.mark.parametrize("date, expected", testdates)
def test_is_working_day(date, expected):
    ret = terminal.is_working_day(date)
    assert ret == expected


@pytest.mark.skip(reason="no way of currently testing this")
def test_open_terminal():
    # I'm not testing this because I can't think another way opening the Windows Terminal other than
    # copying and pasting the func lines. So the test would test if the func is written as it is written
    assert True == True
