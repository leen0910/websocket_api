import json_tools

def jsonDiff(a,b):
    result=json_tools.diff(a,b)
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



if __name__=="__main__":
    jsonDiff()