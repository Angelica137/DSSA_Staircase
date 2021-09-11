from scripts.exercise2 import staircase_d


def test_staircase_d_n_1_returns_1():
    assert staircase_d(1) == 1


def test_staircase_d_n_2_returns_2():
    assert staircase_d(2) == 2


def test_staircase_d_n_3_return_4():
    assert staircase_d(3) == 4


def test_staircase_d_4_return_7():
    assert staircase_d(4) == 7


def test_staircase_d_5_return_13():
    assert staircase_d(5) == 13


def test_staircase_d_20_return_121415():
    assert staircase_d(20) == 121415
