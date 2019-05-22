#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import json
import time




class websocket_request(unittest.TestCase):
    """29. 设置脚本断点 & 30. 清除脚本断点"""
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
        """29. 设置脚本断点 & 30. 清除脚本断点/1. 发送数据 """
        rm=read_message.ReadMessage()
        data_c=rm.get_data("5","control")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_c)
        time.sleep(1)

        # data=rm.get_data("3","initialize")
        # print("step 2、初始化：")
        # c.checkAction(url,data)
        # time.sleep(8)

        data_set_breakpoint=rm.get_data("29","set_breakpoint")
        print("step 3、设置脚本断点")

        data_dict=json.loads(data_set_breakpoint)
        data_dict["data"]=[20,30,32]
        print("设置断点位置："+str(data_dict["data"]))
        data_set_breakpoint=json.dumps(data_dict)
        print(data_set_breakpoint)
        c.checkAction(url,data_set_breakpoint)
        time.sleep(2)

        data_clean_breakpoint=rm.get_data("30","clean_breakpoint")
        print("step 4、清空脚本断点")
        c.checkAction(url,data_clean_breakpoint)
        time.sleep(2)

        # data_script_start=rm.get_data("1","run_script_start")
        # print("step 5、运行脚本：move.lua：")
        # c.checkAction(url,data_script_start)
        # time.sleep(5)
        #
        # data_script_stop=rm.get_data("1","run_script_stop")
        # print("step 6、停止脚本运行：")
        # c.checkAction(url,data_script_stop)

        data_r=rm.get_data("6","release")
        print("step 7、释放设备：")
        c.checkAction(url,data_r)


    def tearDown(self):
        self.ws.close()

if __name__ == "__main__":
    unittest.main()