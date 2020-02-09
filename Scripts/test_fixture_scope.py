'''
@pytest.fixture(scope="function")
# "function"(default):作用于每个测试方法，每个test都运行一次
# "class":作用于整个类，每个class的所有test只运行一次
"""编写插件使用"""
# "module":作用于整个模块，每个module的所有test只运行一次
# "session":作用于整个session(慎用)，每个session只运行一次
'''
# 函数级别
import pytest


@pytest.fixture(scope="function", autouse=True)  # scope="function"
# 每个测试方法之前都会运行一次
def login():
    print("\n 登录")


class Test_003:

    def test_001(self):
        print("\n 进入个人中心")

    def test_002(self):
        print("\n 查看订单")


# 类级别
import pytest


@pytest.fixture(scope="class", autouse=True)  # scope="class"每个测试类之前都会运行一次
def login():
    print("\n 登录")


class Test_004:

    def test_001(self):
        print("\n 进入个人中心")

    def test_002(self):
        print("\n 查看订单")
