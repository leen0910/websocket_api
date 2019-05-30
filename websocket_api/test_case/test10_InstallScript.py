#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time
import json




class websocket_request(unittest.TestCase):
    """32. 安装脚本"""
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

    def test_install_script(self):
        """32. 安装脚本/32.1. 发送数据 """
        rm=read_message.ReadMessage()
        data_c=rm.get_data("5","control")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_c)
        time.sleep(1)

        data_initialize=rm.get_data("3","initialize")
        print("step 2、初始化：")
        c.checkAction(url,data_initialize)
        time.sleep(8)

        data_install_script=rm.get_data("32","install_script")

        """重新设置安装文件名"""
        data_dict=json.loads(data_install_script)
        data_dict["data"]["index"]=1
        data_dict["data"]["name"]="test.lua"
        print("安装脚本："+data_dict["data"]["name"])
        data_install_script=json.dumps(data_dict)
        print(data_install_script)

        print("step 3、安装test.lua文件")
        c.checkAction(url,data_install_script)
        time.sleep(2)

        data_script_start=rm.get_data("1","run_script_start_test")
        print("step 4、运行step 3安装的脚本：test.lua：")
        c.checkAction(url,data_script_start)
        time.sleep(6)

        data_script_stop=rm.get_data("1","run_script_stop")
        print("step 5、停止脚本运行：")
        c.checkAction(url,data_script_stop)

        data_r=rm.get_data("6","release")
        print("step 6、释放设备：")
        c.checkAction(url,data_r)


    def tearDown(self):
        self.ws.close()

if __name__ == "__main__":
    unittest.main()