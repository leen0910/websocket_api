#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c




class websocket_request(unittest.TestCase):
    """8. 修改设备信息"""
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

    def test_config(self):
        """8. 修改设备信息/8.1. 发送数据 """
        rm=read_message.ReadMessage()
        data_c=rm.get_data("5","control")
        url=self.ws
        print("发送“控制设备”数据：")
        c.checkAction(url,data_c)
        data_config=rm.get_data("8","config")
        print("发送“修改设备信息”数据：")
        c.checkAction(url,data_config)
        data_r=rm.get_data("6","release")
        print("发送“释放设备”数据：")
        c.checkAction(url,data_r)


    def tearDown(self):
        self.ws.close()

if __name__ == "__main__":
    unittest.main()
