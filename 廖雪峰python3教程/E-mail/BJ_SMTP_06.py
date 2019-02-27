# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# 参考url = 'https://blog.csdn.net/SL_World/article/details/86368760'
# 同时支持Plain和HTML格式

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input('From:')
password = input('Password:')
# 输入收件人地址：
to_addr = input('To:')
# 输入SMTP服务器地址：
smtp_server = input('SMTP server:')

# 邮件对象：
msg = MIMEMultipart('alternative') # 二选一
msg['From'] = _format_addr('Python爱好者<%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()


msg.attach(MIMEText('hello', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))


server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()


"""
常用邮箱SMTP加密方式:

使用上述SMTP协议发送邮件实则发送的是明文邮件，如果想要加密，有如下几种方式。
1）明文传输:　端口号是25。
server = smtplib.SMTP(smtp_sever,25)

2）SSL加密: 端口号是465，通信过程加密，邮件数据安全。
server = smtplib.SMTP_SSL(smtp_sever,465)

3）TLS加密: 端口号是587，通信过程加密，邮件数据安全，使用正常的smtp端口。对于TLS加密方式需要先建立SSL连接，然后再发送邮件。此处使用starttls()来建立安全连接
server = smtplib.SMTP(smtp_sever,587)
server.starttls()
"""