# -*- coding: utf-8 -*-
# 打开文件

fr=open('心经繁.txt','r', encoding='UTF-8')
# 读取文件所有行
content=fr.readlines()
contentLines=''

characers=[]#存放不同字的总数
rate={}#存放每个字出现的频率
exclude_str = "，。！？、（）【】<>《》=：+-*—“”…"  #除去标点符号

print("心经内容：")
# 依次迭代所有行
for line in content:
    # 去除空格
    line=line.strip()
    print("\033[0;31;40m\t%s\033[0m"%line)
    #如果是空行，则跳过
    if len(line)==0:
        continue
    contentLines = contentLines + line
    # 统计每一字出现的个数
    for x in range(0,len(line)):
        if line[x] not in exclude_str:
            # 如果字符第一次出现 加入到字符数组中
            if not line[x] in characers:
                characers.append(line[x])
            # 如果是字符第一次出现 加入到字典中
            if line[x] not in rate:
                rate[line[x]]=1
            #出现次数加一
            rate[line[x]]+=1

# 对字典进行倒数排序 从高到低 其中e表示dict.items()中的一个元素，
# e[1]则表示按 值排序如果把e[1]改成e[0]，那么则是按键排序，
# reverse=False可以省略，默认为升序排列
rate=sorted(rate.items(), key=lambda e:e[1], reverse=True)

print('全文共有%d个字'%len(contentLines))
print('一共有%d个不同的字'%len(characers))
print()
for i in rate:
    print("\033[32m[",i[0],"] 共出现 ",  i[1], "次")

fr.close()
