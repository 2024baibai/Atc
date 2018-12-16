#-*- coding=utf-8 -*-
import requests
from PIL import Image
import sys
from config import *
if sys.version_info[2]==2:
    import StringIO
else:
    import io as StringIO


upload_url = 'http://api.yundama.com/api.php?method=upload'
query_url = 'http://api.yundama.com/api.php?method=result&cid='



###
error_dict={1001:'密码错误',
-1002:'软件ID/密钥有误',
-1003:'用户被封',
-1004:'IP被封',
-1005:'软件被封',
-1006:'登录IP或软件ID与绑定的不匹配',
-1007:'账号余额为零',
-2001:'验证码类型(codetype)有误',
-2002:'验证码图片太大',
-2003:'验证码图片损坏',
-2004:'上传验证码图片失败',
-3001:'验证码ID不存在',
-3002:'验证码正在识别',
-3003:'验证码识别超时',
-3004:'验证码看不清',
-3005:'验证码报错失败',
-4001:'充值卡号不正确或已使用',
-5001:'注册用户失败'}

def upload(img):
    data = {
        'username': YUNDAMA_USERNAME,
        'password': YUNDAMA_PASSWORD,
        'codetype': '1005',
        'appid': '1',
        'appkey': '22cc5376925e9387a23cf797cb9ba745',
        'timeout': '60',
        'method': 'upload'
    }
    file_ = {'file': open(img,'rb')}
    r = requests.post(upload_url, data=data, files=file_)
    retdata = r.json()
    if retdata["ret"] == 0:
        print(u'上传成功')
        return retdata['cid']
    else:
        print(u'上传失败:{}'.format(error_dict[retdata['ret']]))
        return False


def query_cid(cid):
    url = query_url + str(cid)
    while 1:
        r = requests.get(url)
        retdata = r.json()
        if retdata["ret"] == 0:
            code = retdata["text"]
            print(u'识别验证码：{}'.format(code))
            return code
            break


def captch(img):
    cid = upload(img)
    if cid != False:
        code = query_cid(cid)
        return code
    else:
        return 'abcd'
