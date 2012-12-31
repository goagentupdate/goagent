#!/usr/bin/env python
# coding=utf-8
# Contributor:
# Phus Lu <phus.lu@gmail.com>
# Wang Wei Qiang <wwqgtxx@gmail.com>

__uploaddir__ = 'python' # Which Dir You Need To Upload
__proxy__= '' # Your Proxy Server Address
__need_cookies__= False # If You Want Don't Remove .appcfg_cookies,Please Set "__need_cookies__= True"


import sys,os
print('===============================================================')
print('GoAgent服务端部署程序, 开始上传'+__uploaddir__+'服务端')
print('===============================================================')
print('')
print('请输入您的appid, 多个appid请用|号隔开')
if __need_cookies__== False:
    if os.path.isfile('.appcfg_cookies'):
        os.remove('.appcfg_cookies') 
os.putenv('uploaddir', __uploaddir__)
os.putenv('http_proxy', __proxy__)
os.putenv('https_proxy', __proxy__)
sys.path.insert(0, 'uploader.zip')
import appcfg;appcfg.main()
print('')
print('上传成功，请不要忘记编辑proxy.ini把你的appid填进去，谢谢。按任意键退出程序')

