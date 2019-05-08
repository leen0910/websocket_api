#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time




class websocket_request(unittest.TestCase):
    """9. 操作模式切换"""
    def setUp(self):
        rt=read_info.ReadInfo()
        web=rt.get_device_ip()
        port=rt.get_port()
        url=web+":"+port
        try:
            self.ws=create_connection(url,timeout=5)    #建立设备连接
            if self.ws.connected:
                print("服务：%s连接成功!"%url)
        except Exception as e:
            print("websocket连接失败：%s"%e)
            pass

    def test_control_mode(self):
        """9.1切换debug/user模式 """
        rm=read_message.ReadMessage()
        data_c=rm.get_data("5","control")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_c)
        time.sleep(1)

        data_mode_debug=rm.get_data("9","control_mode_debug")
        print("step 2、切换为debug模式：")
        c.checkAction(url,data_mode_debug)
        time.sleep(1)

        data_mode_user=rm.get_data("9","control_mode_user")
        print("step 3、切换为user模式：")
        c.checkAction(url,data_mode_user)
        time.sleep(1)

        data_clear_error=rm.get_data("clear","clear_all_error")
        print("step 4、清除错误：")
        c.checkAction(url,data_clear_error)
        time.sleep(1)

        data_initialize=rm.get_data("3","initialize")
        print("step 5、初始化：")
        c.checkAction(url,data_initialize)
        time.sleep(10)

        data_r=rm.get_data("6","release")
        print("step 6、释放设备：")
        c.checkAction(url,data_r)


    def tearDown(self):
        self.ws.close()

if __name__ == "__main__":
    unittest.main()