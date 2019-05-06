import configparser

class ReadMessage:
    """定义读取配置的类"""
    def __init__(self):
        self.cf=configparser.ConfigParser()
        self.cf.read("C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api\\message.txt",encoding='UTF-8')  # 配置文件的目录

    def get_data(self,session,key):
        data=self.cf.get(session, key)
        return data




if __name__ == '__main__':
    test = ReadMessage()
    test.__init__()
    c=test.get_data("5","control")
    print(c)