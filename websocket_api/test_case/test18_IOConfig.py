#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
from common import json_diff as d
import time

import json




class websocket_request(unittest.TestCase):
    """19. 读取io配置信息 & 23. 修改io配置信息 """
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

    def test_io_config(self):
        """写入io配置文件，再读取文件。两次文件比较 """
        rm=read_message.ReadMessage()
        data_c=rm.get_data("5","control")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_c)
        time.sleep(1)

        data_write_io=rm.get_data("23","write_io")
        print("step 2、写入io配置信息：")
        c.checkAction(url,data_write_io)
        time.sleep(1)

        print("step 3、读取io配置信息：")
        data_read_io=rm.get_data("19","read_io")
        t=c.checkAction(url,data_read_io)
        time.sleep(1)

        print("step 4、比较第二步和第三步的数据差异：")
        data_write_motion=json.loads(data_write_io)
        a=data_write_motion["data"]
        b=t["data"]
        d.jsonDiff(a,b)
        # d.json_diff(a,b)


        print("step 5、列出io功能数据：")
        lenth=len(t["data"]["function"])
        for i in range(0,lenth):
            print(t["data"]["function"][i])


        print("step 6、释放设备：")
        data_r=rm.get_data("6","release")
        c.checkAction(url,data_r)


    def tearDown(self):
        self.ws.close()

if __name__ == "__main__":
    unittest.main()