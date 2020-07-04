import pytest


@pytest.fixture(scope="function", autouse="True")
def PreStart():
    print("【开始计算】")
    yield
    print("\n【计算结束】")
