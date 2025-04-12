from spam import Spam


def test_spam():
    assert Spam(42).eggs == 42
