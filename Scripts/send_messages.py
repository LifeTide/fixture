"""
启动android手机模拟器发送短信
    循环发送三个内容： hello good  night
"""
import pytest
from appium import webdriver

@pytest.fixture(params=["hello", "good", "night"])
def sms_data(request):
    """返回测试数据"""
    return request.param

class TestSMS:

    def setup_class(self):
        """声明driver"""
        # server 启动参数
        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.101:5555'
        # app信息
        desired_caps['appPackage'] = 'com.android.mms'
        desired_caps['appActivity'] = '.ui.ConversationList'

        # 声明我们的driver对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def teardown_class(self):
        """退出driver"""
        self.driver.quit()

    @pytest.fixture(scope="class", autouse=True)
    def goto_sms(self):
        """进入短信页面"""
        # 点击添加短信按钮 id com.android.mms:id/action_compose_new
        self.driver.find_element_by_id("com.android.mms:id/action_compose_new").click()
        # 输入手机号 id com.android.mms:id/recipients_editor
        self.driver.find_element_by_id("com.android.mms:id/recipients_editor").send_keys('13523451234')

    def test_send_sms(self, sms_data):    # 获取fixture的params参数
        """发送短信"""
        # 输入短信内容 id     com.android.mms:id/embedded_text_editor
        self.driver.find_element_by_id("com.android.mms:id/embedded_text_editor").send_keys(sms_data)
        # 点击发送按钮 id com.android.mms:id/send_button_sms
        self.driver.find_element_by_id("com.android.mms:id/send_button_sms").click()
        #　获取发送结果 ids com.android.mms:id/text_view
        results = self.driver.find_elements_by_id("com.android.mms:id/text_view")
        # 断言
        assert sms_data in [i.text for i in results]