#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time




class websocket_request(unittest.TestCase):
    """1. 脚本运行 & 2. 修改运行速度 & 4. 运行模式切换"""
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

    def test_run_script(self):
        """1. 脚本运行/1.1. 发送数据 """
        rm=read_message.ReadMessage()
        data_c=rm.get_data("5","control")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_c)
        time.sleep(2)

        data_initialize=rm.get_data("3","initialize")
        print("step 2、初始化：")
        c.checkAction(url,data_initialize)
        time.sleep(8)

        # data_mode=rm.get_data("4","move_mode_script")
        # print("step 3、切换为脚本mode：")
        # c.checkAction(url,data_mode)
        # time.sleep(1)

        data_script_start=rm.get_data("1","run_script_start")
        print("step 4、运行脚本：move.lua：")
        c.checkAction(url,data_script_start)
        time.sleep(4)

        data_velocity=rm.get_data("2","run_velocity")
        print("step 5、调节运行速度为50%")
        c.checkAction(url,data_velocity)
        time.sleep(5)

        data_script_pause=rm.get_data("1","run_script_pause")
        print("step 6、暂停脚本运行：")
        c.checkAction(url,data_script_pause)
        time.sleep(2)

        data_script_continue=rm.get_data("1","run_script_continue")
        print("step 7、暂停后继续脚本运行：")
        c.checkAction(url,data_script_continue)
        time.sleep(4)

        data_script_stop=rm.get_data("1","run_script_stop")
        print("step 8、停止脚本运行：")
        c.checkAction(url,data_script_stop)

        data_r=rm.get_data("6","release")
        print("step 9、释放设备：")
        c.checkAction(url,data_r)


    def tearDown(self):
        self.ws.close()

if __name__ == "__main__":
    unittest.main()