'''
fixture参数化
@pytest.fixture(params=None)
    params:要求是list类型
    params:可以为元组，单数不推荐，因为当元组只有一个值时，很多人容易忘记逗号 (1,)
    作用：
        可以提供《基础》的测试数据

fixture(params=[])装饰函数时：
    会让装饰的工厂函数运行的次数 等于 params列表长度

获取fixture(params=[])列表值固定格式
@pytest.fixture(params=[1, 2, 3, 4])
def data(request):  # 固定参数
    """返回测试数据，目的：让测试方法运行多次，可以产生多个测试结果"""
    return request.param    # 固定格式 相当于每次取列表中的一个值
'''
# 代码：
import pytest
@pytest.fixture(params=[1, 2, 3, 4])
def data(request):  # 固定参数
    """返回测试数据，目的：让测试方法运行多次，可以产生多个测试结果"""
    return request.param    # 固定格式 相当于每次取列表中的一个值

class Test_001:

    # def test_001(self):     # 一个方法只能产生一个测试结果
    #     """
    #     列表：[1, 2, 3, 4]
    #     :return:
    #     """
    #     # 列表
    #     lis = [1, 2, 3, 4]
    #     # 遍历
    #     for i in lis:
    #         # 断言
    #         assert i != 2

    def test_001_1(self, data):
        """
        判断列表所有值不等于2
        :param data: 等于 fixture参数params提供的列表中的单个值
        :return:
        """
        # 打印data数据
        print("\n data={}".format(data))
        # 断言
        assert data != 2