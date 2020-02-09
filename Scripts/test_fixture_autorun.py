'''
@pytest.fixture(autouse=True)
作用：装饰的工厂函数不需要调用，会在每个测试方法前自动运行
'''
import pytest
@pytest.fixture(autouse=True) # autouse=True时 login工厂函数不需要调用，会自动运行
def login():
    print("\n 登录")

class Test_001:

    def test_001(self):
        print("\n test_001")

    def test_002(self):
        print("\n test_002")
