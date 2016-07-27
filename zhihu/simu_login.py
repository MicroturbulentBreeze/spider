# -*- coding:utf-8 -*-

import urllib, urllib2, re, cookielib

# 账号相关参数
username = 'yourusername'
password = 'yourpassword'

# 打开目标链接，获取Html
url = 'http://www.zhihu.com'
zhihu = urllib.urlopen(url)
contents = zhihu.read()
# print(contents)
# 获取xsrf值
reg = r'name="_xsrf" value="(.*)"/>'
pattern = re.compile(reg)
result = pattern.findall(contents)
xsrf = result[0]
# 保存cookie
lgurl = 'http://www.zhihu.com/login'
cookie = cookielib.CookieJar()
print cookie
cookie_handler = urllib2.HTTPCookieProcessor(cookie)
hdr = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36'}
post_data = {'_xsrf':xsrf, 'email':username, 'password':password, 'rememberme':'y'}
dt = urllib.urlencode(post_data)
req = urllib2.Request(lgurl, dt, hdr)
opener = urllib2.build_opener(cookie_handler)
urllib2.install_opener(opener)
response = opener.open(req)
page = response.read()
# print(page)
testurl = 'http://www.zhihu.com/settings/account'
req = urllib2.urlopen(testurl)
print(req.read())

