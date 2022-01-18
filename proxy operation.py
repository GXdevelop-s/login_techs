# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2022年01月17日
"""
import requests

if __name__ == '__main__':
    url = 'https://www.baidu.com/s?wd=ip'
    head = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36'
    }
    proxy = {
        'https://':'222.129.39.38'
    }
    response = requests.get(url=url, headers=head, proxies=proxy).text
    with open('../gotpages/ip.html', 'w', encoding='utf-8') as stream:
        stream.write(response)
