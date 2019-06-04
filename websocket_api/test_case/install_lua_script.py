#!/usr/bin/python
'''
./    当前目录（当前文件）
../  上级目录（上级文件）
'''
from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
from common import Base_64
from common import split_read as s
import time
import json




class install(unittest.TestCase):
    """安装脚本文件"""
    filename="move.lua"
    path='../scripts/move.lua'
    index=3
    def setUp(self):
        rt=read_info.ReadInfo()
        web=rt.get_device_ip()
        port=rt.get_port()
        url=web+":"+port
        try:
            # self.ws=create_connection(url,timeout=5)
            self.ws=create_connection(url)    #建立设备连接
            if self.ws.connected:
                print("服务：%s连接成功!"%url)
        except Exception as e:
            print("websocket连接失败：%s"%e)
            pass

    def test_install(self):
        """11. 控制器接收文件/11.1. 发送数据 """
        rm=read_message.ReadMessage()
        data_c=rm.get_data("5","control")
        url=self.ws
        path=self.path
        filename=self.filename
        print("step 1、控制设备：")
        c.checkAction(url,data_c)
        time.sleep(1)

        print("step 2、向设备写入脚本：")

        # """一个总包直接传输文件"""
        # f=open(path,'r',encoding='utf-8')
        # str=f.read()
        # script_base64=Base_64.encode(str)
        # f.close()
        # data_file={
        #     "action":"device.file.receive",
        #     "data":{
        #         "type":"script",
        #         "file_name":filename,
        #         "md5":"",
        #         "total":1,
        #         "index":1,
        #         "content":script_base64
        #         }
        #     }
        # data_file=json.dumps(data_file)
        # c.checkAction(url,data_file)


        """分包写入文件"""
        Block_Size=300*1024
        total=s.total_count(path,Block_Size)
        print(total)
        index=1
        for content in s.read_file(path,Block_Size):
            str=content
            script_base64=Base_64.encode(str)
            data_file={
                "action":"device.file.receive",
                "data":{
                    "type":"script",
                    "file_name":filename,
                    "md5":"",
                    "total":total,
                    "index":index,
                    "content":script_base64
                    }
                }
            data_file=json.dumps(data_file)
            c.checkAction(url,data_file)
            index=index+1
            print(script_base64)


        data_install_script=rm.get_data("32","install_script")

        """重新设置安装文件名"""
        data_dict=json.loads(data_install_script)
        data_dict["data"]["index"]=self.index
        data_dict["data"]["name"]="%s"%filename
        print("安装脚本："+data_dict["data"]["name"])
        data_install_script=json.dumps(data_dict)
        print(data_install_script)

        print("step 3、安装%s文件"%filename)
        c.checkAction(url,data_install_script)
        time.sleep(2)

    #     data_initialize=rm.get_data("3","initialize")
    #     print("step 3、初始化：")
    #     c.checkAction(url,data_initialize)
    #     time.sleep(10)
    #
    #     data_mode=rm.get_data("4","move_mode_script")
    #     print("step 4、切换为脚本mode：")
    #     c.checkAction(url,data_mode)
    #     time.sleep(1)
    #
    #     print("step 5、运行step 2写入的脚本：")
    #     data_script_start={
    # "action" : "device.run.script",
    # "data" :
    # {
    #     "script_name" : filename,
    #     "cmd" : "start"
    # }
    # }
    #     data_script_start=json.dumps(data_script_start)
    #     c.checkAction(url,data_script_start)
    #     time.sleep(500)
    #
    #     data_script_stop=rm.get_data("1","run_script_stop")
    #     print("step 6、停止脚本运行：")
    #     c.checkAction(url,data_script_stop)
    #     time.sleep(2)
    #
    #     print("step 7、删除step 2写入的脚本：")
    #     data_delete_script={
    # "action" : "device.script.delete",
    # "data" :
    # {
    #     "name" : filename
    # }
    # }
    #     data_delete_script=json.dumps(data_delete_script)
    #     c.checkAction(url,data_delete_script)
    #
    #
    #     data_r=rm.get_data("6","release")
    #     print("step 8、释放设备：")
    #     c.checkAction(url,data_r)



    def tearDown(self):
        self.ws.close()

if __name__ == "__main__":
    unittest.main()
    # t=install()
    # t.setUp()
    # t.install_lua_script()