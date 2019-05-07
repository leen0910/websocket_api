#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c




class websocket_request(unittest.TestCase):
    """7. 查询设备信息 """
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

    def test_info_read(self):
        """7. 查询设备信息/7.1. 发送数据 """
        rm=read_message.ReadMessage()
        data=rm.get_data("7","info_read")   # 获取device.info.read命令发送数据包。
        ws=self.ws
        print("发送“查询设备信息”数据：")
        c.checkAction(ws,data)
        # data=json.dumps(message)
        # try:
        #     self.ws.send(message)
        #     for i in range(1,10):
        #         t=self.ws.recv()
        #         t=json.loads(t)
        #         if t["action"]=="device.info.read":
        #             print("返回action：device.info.read的数据：")
        #             print(t)
        #             if t["success"]==bool(1):
        #                 print("device.info.read返回数据成功。")
        #             else:
        #                 print("device.info.read返回数据失败。")
        #             break
        #         else:
        #             print("返回数据错误！")
        #             print(t)
        # except Exception as e:
        #     print("device.info.read命令发送失败：%s"%e)
        #     pass

    def tearDown(self):
        self.ws.close()

if __name__ == "__main__":
    # unittest.main()
    r=websocket_request()
    r.setUp()
    r.test01_info_read()
    # r.tearDown()
