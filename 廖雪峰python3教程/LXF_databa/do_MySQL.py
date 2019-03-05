# !/usr/bin/env python3
# -*- coding:utf-8 -*

# 教程里推荐安装pip install mysql-connector,但会出错因为MySQL8.0版本太高
# 报错:caching_sha2_password , 所以推荐安装 pip install mysql-connector-python 即可得到正确结果

# 导入MySQL驱动:
import mysql.connector
# 注意把password设为你的口令:
conn = mysql.connector.connect(user='root', password='password', database='test')
cursor = conn.cursor()
# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
print(cursor.rowcount)
# 提交事务:
conn.commit()
cursor.close()
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s',('1',))
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection:
cursor.close()
conn.close()