# 类级别工厂函数和类级别初始化函数之间特殊关系
# 特例1
import pytest

'''工厂函数在类外部设置为类级别并自动运行，运行结果为在整个类开始运行工厂函数'''
@pytest.fixture(scope="class", autouse=True)    # scope="function"每个测试方法之前都会运行一次
def login():
    print("\n 开始")

class Test_001:

    def setup_class(self):
        print("\n setup_class")

    def test_001(self):
        print("\n 测试例001")

    def test_002(self):
        print("\n 测试例002")





# 特例2
import pytest

'''工厂函数在类内部设置类级别并自动运行，运行结果为在整个类的setup_class之后优先运行'''

class Test_002:

    def setup_class(self):
        print("\n setup_class")

    def test_001(self):
        print("\n 测试例001")

    def test_002(self):
        print("\n 测试例002")

    @pytest.fixture(scope="class", autouse=True)    # scope="function" 每个方法之前都会运行一次
    def login(self):
        print("\n 开始")