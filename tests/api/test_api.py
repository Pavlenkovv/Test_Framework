import pytest


@pytest.mark.check
def test_check_math():
    assert 7 * 7 == 49


@pytest.mark.change
def test_remove_name(user):
    user.name = ''
    assert user.name == ''


@pytest.mark.check
def test_name(user):
    assert user.name == "Viacheslav"


@pytest.mark.check
def test_second_name(user):
    assert user.second_name == "Butenko"
