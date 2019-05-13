import os
import sys
import os.path

def file_name_all(file_dir,filename):
    for root, dirs, files in os.walk(file_dir):
        print(root) #当前目录路径
        print(dirs) #当前路径下所有子目录
        print(files) #当前路径下所有非目录子文件
        fopen = open(filename, 'w')  # r只读，w可写，a追加
        for file in files:
            if os.path.splitext(file)[1] == '.py':
                fopen.write(file+ '\n')
    fopen.close()




if __name__ == '__main__':
    dir=".\\"
    filename="file_name.txt"
    file_name_all(dir,filename)
    # file_name(dir)
    # listdir(dir)