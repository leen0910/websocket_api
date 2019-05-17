#!/usr/bin/python

from websocket import create_connection

from common import read_info
import json





def ws_connect():
    rt=read_info.ReadInfo()
    web=rt.get_device_ip()
    port=rt.get_port()
    url=web+":"+port
    try:
        ws=create_connection(url,timeout=5)    #建立设备连接
        while(1):
            if ws.connected:
                print("服务：%s连接成功!"%url)
                t=json.loads(ws.recv())
                print(t)
    except Exception as e:
        print("websocket连接失败：%s"%e)
        pass


if __name__ == "__main__":
    ws_connect()
