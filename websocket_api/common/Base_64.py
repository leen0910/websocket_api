import base64


def encode(str):
    #base64编码
    encodestr = base64.b64encode(str.encode('utf-8')) #转成bytes string
    encodestr=encodestr.decode()
    return encodestr

def decode(str):
    #解码

    decodestr = base64.b64decode(str.encode('utf-8'))
    decodestr = decodestr.decode()
    return decodestr


if __name__=="__main__":
    print(encode("我是字符串"))
    print(decode(encode("我是字符串")))
