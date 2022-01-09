# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2022年01月09日
"""
# 需求：要求通过验证码识别，用程序登录人人网并查看响应码
import requests
from lxml import etree
from chaojiying_Python import chaojiying

if __name__ == '__main__':
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    head = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36'
    }
    page_text = requests.get(url=url, headers=head).text
    tree = etree.HTML(page_text)
    verification_src = tree.xpath('//*[@id="imgCode"]/@src')[0]
    with open(r'../gotpages/verification.jpg', 'wb') as stream:
        verification_url = 'https://so.gushiwen.cn' + verification_src
        pic_binary = requests.get(url=verification_url, headers=head).content
        stream.write(pic_binary)
    chaojiying = chaojiying.Chaojiying_Client('gxnbgxnb', 'Kissmyass0', '927371')  # 用户中心>>软件ID 生成一个替换 96001
    im = open('../gotpages/verification.jpg', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    # 验证码识别完成
    pic_code = chaojiying.PostPic(im, 1004)['pic_str']  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    # 准备登录参数
    # 在打开古诗文网的时候，遇到了审查页面元素是否打开了开发者工具devtools，没能获取到login包中的参数信息，无法准备登录参数
    params={

    }
    login_url=''
    response=requests.post(url=login_url,headers=head)
    # 查看响应码
    print()
