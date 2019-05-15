import json_tools
import jsondiff
import json
from collections import Iterable

def jsonDiff(a,b):
    result=json_tools.diff(a,b)
    if result==[]:
        print("两个数据内容一致：%s"%result)
    else:
        print("两个数据内容存在不一致：%s"%result)

def json_diff(a,b):
    """第三方库，对于嵌套json数据进行比较"""
    result=jsondiff.diff(a,b)
    if result==[]:
        print("两个数据内容一致：%s"%result)
    else:
        print("两个数据内容存在不一致：%s"%result)


def cmp(src_data,dst_data):
    if isinstance(src_data,dict):
        for key in dst_data:
            if key not in src_data:
                print("src不存在这个key:"+key)
        for key in src_data:
            if key in dst_data:
                thiskey=key

                cmp(src_data[thiskey],dst_data[thiskey])
            else:
                print("src不存在这个key:"+key)
    elif isinstance(src_data,list):
        if len(src_data)!=len(dst_data):
            print("list的长度不相等！")
        for src_list,dst_list in zip(src_data,dst_data):
            cmp(src_list,dst_list)
    else:
        if str(src_data)!=str(dst_data):
            print(src_data)



def isEqual(value1,value2):
    if type(value1)!=type(value2):
        print("111111")
        return False
    if isinstance(value1,Iterable):
        if len(value1)!=len(value2):
            print("2222222222")
            return False
        if isinstance(value1,dict):
            for key in value1:
                if key not in value2:
                    print("33333333333")
                    return False
                if type(value1[key])!=type(value2[key]):
                    print("4444")
                    return False
                if isinstance(value1[key],Iterable):
                    if not isEqual(value1[key],value2[key]):
                        print("5555555555")
                        return False
                elif value1[key]!=value2[key]:
                    print("666666666")
                    return False
        else:
            if len(value1)!=len(value2):
                print("777777777")
                return False
            for index in range(len(value1)):
                if type(value1[index])!=type(value2[index]):
                    print("888888888")
                    return False
                if isinstance(value1[index],Iterable)and type(value1[index])!=str:
                    if not isEqual(value1[index],value2[index]):
                        print("99999999999")
                        return False
                elif value1[index]!=value2[index]:
                    print("00000000000")
                    return False
    else:
        return value1==value2
    return True





if __name__=="__main__":
    jsonDiff()
