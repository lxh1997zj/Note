# !/usr/bin/env python3
# -*- coding:utf-8 -*-
class Field(object):
	def __init__(self,name,column_type):
		self.name = name
		self.column_type = column_type
	def __str__(self):
		return '<%s : %s>' % (self.__class__.__name__,self.name)

class StringField(Field):
	def __init__(self,name):
		super(StringField,self).__init__(name,'varchar(100)')

class IntegerField(Field):
	def __init__(self,name):
		super(IntegerField,self).__init__(name,'bigint')

class ModelMetaclass(type):   # metaclass是类的模板，所以必须从`type`类型派生：
	def __new__(cls,name,bases,attrs):
		if name == 'Model':
			return type.__new__(cls,name,bases,attrs)
		print('Found model : %s' % name)
		mappings = dict()
		for k,v in attrs.items():
			if isinstance(v,Field):
				print('Found mapping : %s ==> %s' % (k,v) )
				mappings[k] = v
		for k in mappings.keys():
			attrs.pop(k)
		attrs['__mappings__'] = mappings     # 保存属性和列的映射关系
		attrs['__table__'] = name       # 假设表名和类名一致
		return type.__new__(cls,name,bases,attrs)

class Model(dict,metaclass=ModelMetaclass):
	def __init__(self,**kw):
		super(Model,self).__init__(**kw)
	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Model' object has no attribute '%s'" % key)
	def __setattr__(self,key,value):
		self[key] = value
	def save(self):
		fields =[]
		params = []
		args = []
		for k,v in self.__mappings__.items():
			fields.append(v.name)
			params.append('?')     # params.append(str(getattr(self,k,404))) SQL的value为实例(instance)的值
			args.append(getattr(self,k,None))
		sql = 'insert into %s (%s) values (%s)' % (self.__table__,','.join(fields),','.join(params))
		print('SQL : %s' % sql)
		print('ARGS : %s' % str(args))

class User(Model):
	# 定义类的属性到列的映射：
	id = IntegerField('id')
	name = StringField('username')
	email = StringField('email')
	password = StringField('password')
# 创建一个实例：
u = User(id=12345,name='Michael',email='test@orm.org',password='my-pwd')
# 保存到数据库：
u.save()



# object.__new__(cls[, ...])是一个定制方法，作用是创建类的实例，第一个参数是类，后面的参数是用于构造实例的所有包括类名，父类和所有构造属性的参数
# 定制方法__new__()在元类定义这里使用的参数具体含义：
# cls表示元类
# name表示创建类的类名（在这里创建类就是继承Model类的子类User）
# bases表示创建类继承的所有父类
# attrs表示创建类的所有属性和方法（以键值对的字典的形式）