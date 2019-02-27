# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# 正文里带图片的邮件

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
msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者<%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('<html><body><h1>Hello</h1>' + '<p><img src="cid:0"></p>' + '</body></html>', 'html', 'utf-8'))

with open('dog.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是jpg类型:
    mime = MIMEBase('image', 'jpg', filename='dog.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='dog.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-ID', '0')
    # 把附件的内容读进来：
    mime.set_payload(f.read())
    # 用Base64编码：
    encoders.encode_base64(mime)
    # 添加到MIMEMutipart:
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

"""
# 在邮件正文里显示图片的第二种方法:
# 在方法一的基础上，直接使用MIMEImage对象处理图片文件，替换MIMEBase对象，仅三行代码ok。修改部分代码如下：
from email.mime.image import MIMEImage
...
with open('/home/sparkfly/Desktop/image.png','rb') as f:
    mimeImage = MIMEImage(f.read())
    mimeImage.add_header('Content-ID', 'Image')
    msg.attach(mimeImage)
...
"""
