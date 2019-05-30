#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time




class websocket_request(unittest.TestCase):
    """31. 查询运行脚本当前行数位置"""
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

    def test_drag(self):
        """31. 查询脚本运行位置/31.1. 发送数据 """
        rm=read_message.ReadMessage()
        data_c=rm.get_data("5","control")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_c)
        time.sleep(1)

        data=rm.get_data("3","initialize")
        print("step 2、初始化：")
        c.checkAction(url,data)
        time.sleep(8)

        data_script_start=rm.get_data("1","run_script_start")
        print("step 3、运行脚本：move.lua：")
        c.checkAction(url,data_script_start)
        time.sleep(3)

        data_query_position=rm.get_data("31","query_position")
        print("step 4、查询运行中的脚本行数位置。")
        c.checkAction(url,data_query_position)
        time.sleep(3)

        data_script_pause=rm.get_data("1","run_script_pause")
        print("step 5、暂停脚本运行：")
        c.checkAction(url,data_script_pause)
        time.sleep(2)

        data_query_position=rm.get_data("31","query_position")
        print("step 6、查询暂停的脚本行数位置。")
        c.checkAction(url,data_query_position)
        time.sleep(3)

        data_script_stop=rm.get_data("1","run_script_stop")
        print("step 7、停止脚本运行：")
        c.checkAction(url,data_script_stop)

        data_r=rm.get_data("6","release")
        print("step 8、释放设备：")
        c.checkAction(url,data_r)


    def tearDown(self):
        self.ws.close()

if __name__ == "__main__":
    unittest.main()