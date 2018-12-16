# Atc：Abbey微博图床计划

### Feature:
1. 上传模式，支持：拖拽文件、点击上传、复制粘贴（截图之后粘贴板有图片信息）
2. 支持批量上传
3. 支持选择图片大小

### 安装使用
1. 下载代码
```
cd /home
git clone https://github.com/abbeyokgo/Atc.git
cd Atc
```

2. 配置账号信息
编辑`config.py`
- 微博账号密码
- 云打码账号密码

ps. 配置云打码是为了自动登录微博。

#### 微博用户名密码
- WEIBO_USERNAME=''
- WEIBO_PASSWORD=''

#### 云打码的用户名、密码
- YUNDAMA_USERNAME = ''
- YUNDAMA_PASSWORD = ''

云打码注册地址：[http://www.yundama.com/index/reg](http://www.yundama.com/index/reg)

**注册之后必须充值！充值1元就能用很久了！**


3. 安装依赖&运行
```
pip install requirements.txt
gunicorn -keventlet -b 0:35000 run:app
```
然后访问:`http://ip:35000`

4. 绑定域名
参考[PyOne文档-绑定域名][https://wiki.pyone.me/pyone-an-zhuang/bang-ding-yu-ming.html]

注意：**端口号**

5. 配置开机启动(仅限**centos7**，其他系统请自行搜索)
**注意目录是否正确**
```
cp supervisord.conf.sample supervisord.conf
echo "supervisord -c /home/Atc/supervisord.conf" >> /etc/rc.d/rc.local
chmod +x /etc/rc.d/rc.local
```


### 预览
![](http://wx4.sinaimg.cn/large/0074MymAgy1fy8eombkyrg31as0oq1gz.gif)