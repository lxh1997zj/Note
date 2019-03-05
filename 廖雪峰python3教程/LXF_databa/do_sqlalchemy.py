# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类：
Base = declarative_base()

# 定义User对象：
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接：
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
# 创建DBSession类型：
DBSession = sessionmaker(bind=engine)

# 创建session对象：
session = DBSession()
# 创建User对象：
new_user = User(id='5', name='Bob')
# 添加到session：
session.add(new_user)
# 提交即保存到数据库：
session.commit()
# 关闭session：
session.close()

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行：
user = session.query(User).filter(User.id == '5').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
# 关闭session：
session.close()



"""
# ORM框架也可以提供两个对象之间的一对多、多对多等功能
# 假设一个User有多个Book

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多,一个人对应多本书
    # 在用户表类中通过 relationship() 方法来引用书表的类集合:
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # '多'的一方的book表是通过外键关联到user表的：
    # 千万要记住 ForeignKey(数据库名.字段名) book表的外键对应的是用户表的id主键,要一定注意大小写:
    user_id = Column(String(20)), ForeignKey('user.id')
# 结果: 当我们查询一个User对象时，该对象的books属性将返回一个包含若干个Book对象的list
"""