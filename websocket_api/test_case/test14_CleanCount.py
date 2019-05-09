#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time

class websocket_request(unittest.TestCase):
    """26. 清除脚本运行次数"""
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

    def test_clean_count(self):
        """26. 清除脚本运行次数/26.1. 发送数据 """
        rm=read_message.ReadMessage()
        data_c=rm.get_data("5","control")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_c)
        time.sleep(1)

        data_clean_count=rm.get_data("26","clean_scriptCount")
        print("step 2、清除“move.lua”脚本运行次数：")
        c.checkAction(url,data_clean_count)
        time.sleep(1)

        data_def_script=rm.get_data("17","read_lua")
        print("step 3、读取lua配置信息查询move.lua运行次数是否被清除：")
        t=c.checkAction(url,data_def_script)
        time.sleep(1)
        lenth=len(t["data"]["file"])
        for i in range(0,lenth):
            if t["data"]["file"][i]["name"]=="move.lua":
                if t["data"]["file"][i]["count"]==0:
                    print("“move.lua”的运行次数成功被清零：%s"%t["data"]["file"][i])
                else:
                    print("“move.lua”的运行次数清除失败：%s"%t["data"]["file"][i])

        data_r=rm.get_data("6","release")
        print("step 4、释放设备：")
        c.checkAction(url,data_r)


    def tearDown(self):
        self.ws.close()

if __name__ == "__main__":
    unittest.main()