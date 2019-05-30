#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time




class websocket_request(unittest.TestCase):
    """4. 运行模式切换"""
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
        """4. 运行模式切换/插补：Interpolation，拖拽：drag """
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

        data_drag=rm.get_data("4","move_mode_drag")
        print("step 3、进入拖拽模式：")
        c.checkAction(url,data_drag)
        time.sleep(3)

        data_interpolation=rm.get_data("4","move_mode_interpolation")
        print("step 4、进入插补模式：")
        c.checkAction(url,data_interpolation)
        time.sleep(2)


        data_r=rm.get_data("6","release")
        print("step 5、释放设备：")
        c.checkAction(url,data_r)


    def tearDown(self):
        self.ws.close()

if __name__ == "__main__":
    unittest.main()