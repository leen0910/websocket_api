#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time




class websocket_request(unittest.TestCase):
    """10. 查询已安装脚本"""
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

    def test_script_query(self):
        """10. 查询已安装脚本/10.1. 发送数据 """
        rm=read_message.ReadMessage()
        data_c=rm.get_data("5","control")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_c)
        time.sleep(1)

        data_script_query=rm.get_data("10","script_query")
        print("step 2、查询已安装脚本：")
        t=c.checkAction(url,data_script_query)
        time.sleep(2)

        print("step 3、准备列出已安装脚本名称：")
        lenth=len(t["data"])
        if lenth != 0:
            print("列出已安装脚本名称：")
            for i in range(0,lenth):
                print(t["data"]["%s"%i])
        else:
            print("查询已安装脚本为空！")


        data_r=rm.get_data("6","release")
        print("step 4、释放设备：")
        c.checkAction(url,data_r)


    def tearDown(self):
        self.ws.close()

if __name__ == "__main__":
    unittest.main()