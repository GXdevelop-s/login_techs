# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2022年01月06日
"""
import requests
from lxml import etree
from chaojiying_Python.chaojiying import Chaojiying_Client

if __name__ == '__main__':
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    head = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)'
    }
    page_text = requests.get(url=url, headers=head).text
    tree = etree.HTML(page_text)
    pic_src = tree.xpath('//*[@id="imgCode"]/@src')[0]
    with open(r'verification.jpg', 'wb') as stream:
        pic_url = 'https://so.gushiwen.cn' + pic_src
        pic_code = requests.get(url=pic_url, headers=head).content
        stream.write(pic_code)  # 验证码是动态的，怎么办

    chaojiying = Chaojiying_Client('gxnbgxnb', 'Kissmyass0', '927371')  # 用户中心>>软件ID 生成一个替换 96001
    im = open('verification.jpg', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    print(chaojiying.PostPic(im, 1902))  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
