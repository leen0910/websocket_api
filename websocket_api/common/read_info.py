import configparser

class ReadInfo:
    """定义读取配置的类"""
    def __init__(self):
        self.cf=configparser.ConfigParser()
        self.cf.read('C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api\\info.txt')  #配置文件的目录

    def get_device_ip(self):
        device_ip=self.cf.get('info', 'device_ip')
        return device_ip

    def get_port(self):
        port=self.cf.get('info', 'port')
        return port



if __name__ == '__main__':
    test = ReadInfo()
    ip = test.get_device_ip()
    port = test.get_port()
    print(ip)
    print(port)