import configparser

class ReadMessage:
    """定义读取配置的类"""
    def __init__(self):
        self.cf=configparser.ConfigParser()
        self.cf.read("C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api\\message.txt")  # 配置文件的目录

    def get_info_read(self):
        info_read=self.cf.get('data', 'info_read')
        return info_read




if __name__ == '__main__':
    test = ReadMessage()
    init = test.get_init()
    print(init)