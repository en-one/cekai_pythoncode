import pytest


@pytest.fixture(scope="function", autouse="True")
def PreStart():
    print("【开始计算】")
    yield
    print("\n【计算结束】")


def pytest_addoption(parser):
    mygroup = parser.getgroup("josiah")
    mygroup.addoption("--env",
                      default='test',
                      dest='env',
                      help='josiah add help'
                      )


@pytest.fixture(scope='session')
def cmdOption(request):
    myenv = request.config.getoption("--env", default='test')
    if myenv == 'test':
        print("获取测试环境配置信息")
    elif myenv == 'dev':
        print("获取开发环境配置信息")
    elif myenv == 'st':
        print("获取ST环境配置信息")


