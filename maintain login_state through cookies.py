# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2022年01月16日
"""

# 需求：要求通过验证码识别，用程序登录红薯网并查看响应码和页面源码
import requests
from lxml import etree
from chaojiying_Python import chaojiying

if __name__ == '__main__':
    url = 'https://i.hongshu.com/login.html?url=https%3A%2F%2Fwww.hongshu.com%2F&sign=1'
    head = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36'
    }
    page_text = requests.get(url=url, headers=head).text
    tree = etree.HTML(page_text)
    verification_src = tree.xpath('//*[@id="imgValidCode"]/@src')[0]
    with open(r'../gotpages/verification.jpg', 'wb') as stream:
        verification_url = verification_src
        pic_binary = requests.get(url=verification_url, headers=head).content
        stream.write(pic_binary)
    chaojiying = chaojiying.Chaojiying_Client('gxnbgxnb', 'Kissmyass0', '927371')  # 用户中心>>软件ID 生成一个替换 96001
    im = open('../gotpages/verification.jpg', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    # 验证码识别完成
    pic_code = chaojiying.PostPic(im, 1004)['pic_str']  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    # 准备登录参数
    params = {
        'username': '1785598676@qq.com',
        'password': '7k7k88@3',
        'validcode': pic_code,
        'url': 'https://www.hongshu.com/',
        'sign': '1',
        'logining': '1'
    }
    login_url = 'https://i.hongshu.com/login.html'
    session = requests.Session()
    login_response = session.post(url=login_url, headers=head)
    # 查看响应码
    print(login_response.status_code)
    # 进入个人页面
    private_tree = etree.HTML(login_response.text)
    private_src = private_tree.xpath('//*[@id="loginInfoForm"]/div/div[1]/span/a/@href')[
        0]  # 这边数组越界，是因为登录之后需要点击操作，第二次登录
    private_text = session.get(url=private_src, headers=head).text
    with open('../gotpages/privateHTML.html', 'w', encoding='utf-8') as stream:
        stream.write(private_text)
