import string
from matplotlib import pyplot as plt
import matplotlib.font_manager as fm

hist=[]

def process_line(line, hist):#生成[50, 'the']等列表
    for word in line.split():
        word = word.strip(string.punctuation+string.whitespace)#去除空格及标点符号
        word.lower()#小写
        if word not in hist:#生成列表并统计个数
            hist[word] = 1
        else:
            hist[word]=hist[word]+1
        #hist[word] = hist.get(word,0) + 1

def process_file(filename):
    res = {}
    with open(filename, 'r',encoding='UTF-8') as f:
        for line in f:
            process_line(line, res)
    return res#返回统计后字典

def most_word(hist, num):
    tmp = []
    for key,value in hist.items():#将key和value互换 排序
        tmp.append([value,key])
    tmp.sort(reverse=True)
    return tmp[:num]#切片

def showtable(data):
    for i in range(len(data)):
        plt.bar(data[i][1:],data[i][:-1])
    ZH = fm.FontProperties(fname='C:\Windows\Fonts\simkai.ttf')
    plt.legend(prop=ZH)  # 完成数据加载
    plt.xlabel(u'单词', fontproperties=ZH)
    plt.ylabel(u'频率', fontproperties=ZH)
    plt.title(u'统计单词出现的频率', fontproperties=ZH)
    #调整图片输出大小
    png_size = plt.gcf()
    png_size.set_size_inches(20.5, 13.5)#宽1850X1050
    png_size.savefig("D:\word.png", dpi=100)
    plt.show()


if __name__ == '__main__':
    hist = process_file("心经繁.txt")
    data = most_word(hist,30)
    print(data)
    showtable(data)