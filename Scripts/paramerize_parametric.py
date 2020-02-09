# import pytest
#
#
# @pytest.mark.parametrize("参数", 参数值)
#     参数说明:
#         参数: 单个  # "name1"
#         参数值: ["参数值1", "参数值2" .......]
#
#         参数: 多个  # "name1, name2"
#         参数值: [("参数1值, 参数2值"), ("参数1值, 参数2值") ..........]
#
#     方法装饰测试方法:
#         测试方法运行的次数 等于  参数值的长度
#         1 参数名字可以自定义
#         2 每一个parametrize参数必须传递到测试方法参数中，可以不使用，但必须传递
#         3 parametrize参数名字必须  等于  测试方法名字
#         4 当多个参数时，在parametrize中参数顺序一定要注意和参数值中元组内value的顺序一致


# 单个参数代码:
import pytest
class Test_ParamOne:
    @pytest.mark.parametrize("num", [1, 2, 3, 4])
    def test_001(self, num):
        """判断列表中所有值和3进行比较"""
        # 打印
        print("\n num={}".format(num))
        # 断言
        assert num != 3

# 多个参数代码
class Test_paramMore:
    @pytest.mark.parametrize("a, b, c", [(1, 2, 3), (2, 4, 5), (4, 5, 9)])
    def test_001(self, a, b, c):
        '''
        加法计算：判断 a b 之和 等于 c
        a + b == c
        :return:
        '''
        # 打印 a b c
        print("\n {} + {} =={}".format(a, b, c))
        # 断言
        assert a + b == c


# 函数返回值方式代码:        （当前主流传递方式）
def data():
    """进行数据解析操作"""
    return [(1, 2, 3), (4, 5, 7), (3, 6, 9)]
class Test_ParamMore:
    @pytest.mark.parametrize("a, b, c", data())     # 函数返回值方式，提供测试数据
    def test_001(self, a, b, c):
        """
        加法计算: 判断 a b 之和 等于 c
        a + b == c
        :return:
        """
        # 打印 a+b==c
        print("\n {} + {} == {}".format(a, b, c))
        # 断言
        assert a + b == c