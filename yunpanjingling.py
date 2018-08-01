# -*- coding: utf-8 -*-
import requests
import re

url = 'https://www.yunpanjingling.com/search/'
keyword = raw_input('请输入搜索关键词：')
page = raw_input('请输入要检索的总页数：')
headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'}

def parse_page(response):
    comment = re.findall('<a href=\"(.*?)\" target', response)
    name= re.findall('rel=\"nofollow\"> (.*?) <\/a>',response)
    return comment,name

num=1
while num<int(page)+1:
    print('---------------第'+str(num)+'页---------------------')
    url=url+keyword+'?page='+str(num)
    response = requests.get(url=url,headers=headers).text
    comment,name = parse_page(response)
    for x, y in zip(name, comment):
        print('\n')
        print(x.replace('<em>','').replace('</em>',''))
        print(y)
    num+=1
    print('\n')