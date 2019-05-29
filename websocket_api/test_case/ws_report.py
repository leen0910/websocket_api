#!/usr/bin/python

from websocket import create_connection

from common import read_info
import json
import signal
from common import read_message
from common import check_action as c
def stop(signum, frame):

  global is_sigint_up
  is_sigint_up = True
  print("catched interrupt signal!")

signal.signal(signal.SIGINT, stop)
# signal.signal(signal.SIGHUP, stop)
signal.signal(signal.SIGTERM, stop)

def ws_connect():
    is_sigint_up = False
    rt=read_info.ReadInfo()
    web=rt.get_device_ip()
    port=rt.get_port()
    url=web+":"+port
    try:
        ws=create_connection(url,timeout=5)    #建立设备连接
        # rm=read_message.ReadMessage()
        # data_query_position=rm.get_data("31","query_position")
        while(is_sigint_up==False):
            if ws.connected:
                print("服务：%s连接成功!"%url)
                t=json.loads(ws.recv())
                print(t)
                # print("查询脚本行数位置。")
                # c.checkAction(ws,data_query_position)
        ws.close()
    except Exception as e:
        print("websocket连接失败：%s"%e)
        pass


if __name__ == "__main__":
    ws_connect()
