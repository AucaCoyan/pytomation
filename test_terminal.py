import terminal


def test_is_working_day(date):
    ret = terminal.is_working_day(date)
    assert ret == False
