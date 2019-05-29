#!/usr/bin/env python
#-*- coding:utf-8 -*-

import json

def checkAction(ws,data):
    data_json=json.loads(data)
    action=data_json["action"]
    try:
        ws.send(data)
        for i in range(1,50):
            t=ws.recv()
            t=json.loads(t)
            if t["action"]==action:
                print("返回action：%s的数据："%action)
                print(t)
                if t["success"]==True:
                    print("%s返回数据成功。"%action)
                else:
                    print("%s返回数据失败。"%action)
                break
        else:
            print("返回数据错误！")
            print(t)
    except Exception as e:
        print("%s命令发送失败：%s"%(action,e))
        pass
    return t
