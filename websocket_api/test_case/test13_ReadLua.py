#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time

class websocket_request(unittest.TestCase):
    """17. 读取lua配置信息"""
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

    def test_read_lua(self):
        """17. 读取lua配置信息/17.1. 发送数据 """
        rm=read_message.ReadMessage()
        data_c=rm.get_data("5","control")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_c)
        time.sleep(1)

        data_read_lua=rm.get_data("17","read_lua")
        print("step 2、读取lua配置信息：")
        t=c.checkAction(url,data_read_lua)
        time.sleep(1)
        lenth=len(t["data"]["file"])
        print("显示lua配置信息列：")
        for i in range(0,lenth):
            if t["data"]["file"][i]["name"]!="":
                print(t["data"]["file"][i])

        data_r=rm.get_data("6","release")
        print("step 3、释放设备：")
        c.checkAction(url,data_r)


    def tearDown(self):
        self.ws.close()

if __name__ == "__main__":
    unittest.main()