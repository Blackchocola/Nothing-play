import re
import urllib
from urllib import request
#分别导入re与urllib库，并从urllib库中导出网页分析模块request

link = re.compile('<h3>.*</h3>')
linker = re.compile('[\>].*[\.]')
#把不同的两个正则赋给两个变量


def first_link(link_start):
    #data = urllib.request.urlopen('http://www.heibanke.com/lesson/crawler_ex00/13579/')
    #data = urllib.request.urlopen('http://www.heibanke.com/lesson/crawler_ex00/{}'.format(number))
    data_read = link_start.read().decode('utf-8')
    date = re.findall(link,data_read)
    date_re = re.findall(linker,str(date))
    return ''.join(date_re)
#该函数为读取，解码网页并利用正则提取出<h3></h3>中的内容并返回

def user_linker(number):
    link_the_first = urllib.request.urlopen('http://www.heibanke.com/lesson/crawler_ex00/{}'.format(number))
    #test = data.read().decode('utf-8')
    #print(test)
    return first_link(link_the_first)
#该函数为将用户所‘得’的数加入’原网页’并返回调用first_link函数的结果

data = urllib.request.urlopen('http://www.heibanke.com/lesson/crawler_ex00/13579/')
print(first_link(data))
#先抓取一个网址用来调用first_link函数。（用来启动整个程序的）

#answer = input('CODE:')
#print(user_linker(int(answer)))
for x in range(4):
    answer = input('CODE:')
    print(user_linker(int(answer)))
#测试程序是否成功
