#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time

class websocket_request(unittest.TestCase):
    """24. 修改modbus配置信息"""
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

    def test_write_modbus(self):
        """24. 修改modbus配置信息/24.1. 发送数据 """
        rm=read_message.ReadMessage()
        data_c=rm.get_data("5","control")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_c)
        time.sleep(1)

        data_write_modbus=rm.get_data("24","write_modbus")
        print("step 2、写入modbus配置文件：")
        c.checkAction(url,data_write_modbus)
        time.sleep(1)

        print("step 3、校验写入的modbus配置文件正确性：")
        data_read_modbus=rm.get_data("20","read_modbus")
        t=c.checkAction(url,data_read_modbus)
        time.sleep(1)
        lenth=len(t["data"]["client"])
        for i in range(0,lenth):
            print(t["data"]["client"][i])
            if t["data"]["client"][i]["ip"]=="192.168.1.20":
                if t["data"]["client"][i]["index"]==1:
                    if t["data"]["client"][i]["port"]==500:
                        if t["data"]["client"][i]["count"]==-1:
                            if t["data"]["client"][i]["enable"]==bool(1):
                                print("写入modbus配置index=1信息正确")
                else:
                    print("写入modbus配置index=1信息错误")
            if t["data"]["client"][i]["ip"]=="192.168.1.111":
                if t["data"]["client"][i]["index"]==2:
                    if t["data"]["client"][i]["port"]==1502:
                        if t["data"]["client"][i]["count"]==-1:
                            if t["data"]["client"][i]["enable"]==bool(1):
                                print("写入modbus配置index=2信息正确")
                else:
                    print("写入modbus配置index=2信息错误")

            if t["data"]["client"][i]["ip"]=="192.168.1.100":
                if t["data"]["client"][i]["index"]==3:
                    if t["data"]["client"][i]["port"]==1502:
                        if t["data"]["client"][i]["count"]==-1:
                            if t["data"]["client"][i]["enable"]==bool(0):
                                print("写入modbus配置index=3信息正确")
                else:
                    print("写入modbus配置index=3信息错误")

            if t["data"]["client"][i]["ip"]=="192.168.1.91":
                if t["data"]["client"][i]["index"]==4:
                    if t["data"]["client"][i]["port"]==1502:
                        if t["data"]["client"][i]["count"]==-1:
                            if t["data"]["client"][i]["enable"]==bool(0):
                                print("写入modbus配置index=4信息正确")
                else:
                    print("写入modbus配置index=4信息错误")

            if t["data"]["client"][i]["ip"]=="10.0.0.102":
                if t["data"]["client"][i]["index"]==5:
                    if t["data"]["client"][i]["port"]==1502:
                        if t["data"]["client"][i]["count"]==20:
                            if t["data"]["client"][i]["enable"]==bool(1):
                                print("写入modbus配置index=5信息正确!")
                else:
                    print("写入modbus配置index=5信息错误")

        data_r=rm.get_data("6","release")
        print("step 4、释放设备：")
        c.checkAction(url,data_r)


    def tearDown(self):
        self.ws.close()

if __name__ == "__main__":
    unittest.main()