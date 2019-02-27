# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# 思考题
# 参考url='https://www.liaoxuefeng.com/discuss/001409195742008d822b26cf3de46aea14f2b7378a1ba91000/0015339383507176c48ef038ff7419d946b68028d4d4c4c000'
'__getattr__():动态返回一个属性'
>>> class Chain(object):
...     def __init__(self,path=''):
...         self._path = path
...     def __getattr__(self,path):
...         return Chain('%s/%s'%(self._path,path))
...     def __str__(self):
...         return self._path
...     __call__ = __getattr__
...     __repr__ = __str__
...
>>> Chain().users('Michael').repos
/users/Michael/repos
>>> Chain().status.user.timeline.list
/status/user/timeline/list

Chain().status.user.timeline.list “敲回车键”
“()”和“.”和“回车键”都是从左向右的顺序运算符，类比成数学中的加和减。
步骤：
1、Chain是类名，对它进行“()”运算，即调用__init__(self)(这个有讲过哦),会生成一个实例c1，c1=Chain(path='')。
2、对实例c1进行“.”运算，增加一个“status”属性，即调用__getattr__(self, status),返回
一个新实例c2,c2=Chain(path='/status')。
3、对实例c2进行“.”运算，增加一个“user”属性，即调用__getattr__(self, user),返回
一个新实例c3,c3=Chain(path='/status/user')。
4、对实例c3进行“.”运算，增加一个“timeline”属性，即调用__getattr__(self, timeline),返回
一个新实例c4,c4=Chain(path='/status/user/timeline')。
5、对实例c4进行“.”运算，增加一个“list”属性，即调用__getattr__(self, list),返回
一个新实例c5,c5=Chain(path='/status/user/timeline/list')。
6、对实例c5进行“回车键”运算，即调用__repr__(self)，返回c5._path,即输出'/status/user/timeline/list'。

这样再来看思考题：Chain().users('michael').repos就很清晰了。
Chain--“()”(即调用__init__)——>c1——“.users”(即调用__getattr__)——>c2——“('michael')”(即调用__call__)——>c3——“.repos”(即调用__getattr__)——>c4——“回车键”(即调用__repr__)——>'/users/michael/repos'。
那么类该怎么写，就不用多说了吧。只比老师的示例多加一个__call__方法：

def __call__(self, param):
        return Chain('%s/%s' % (self._path, param))

嗯，看了楼主的查看明白，,但是当真的有user(param) 这个函数时，会以这个函数有优先，
      def users(self,path):
    return Chain('%s/%s/pppp' % (self._path, path))

    s2 = Chain("www.db.com").users('michael').repos
    print(s2)

   结果 ： www.db.com/michael/pppp/repos


   我当时也是这么理解的,这个相当于递归函数了,只是我没想到两点,第一,这个类可以递归,第二个,这个取属性是以 .分隔的, 我以为.user.name 算做一个属性



Chain().users('michael').repos的例子
像楼主这样理解也是可以的，但是我估计作者的原意应该是执行了Chain().users后返回一个函数，这个函数可以创建并返回一个China类的对象：

def getattr(self, path):
    if path = 'users':
        return lambda x: China('%s/%s/%s' % (self._path, path, x))
    else:
        return China('%s/%s' % (self._path, path))

优秀答案：
class Chain(object):
    def init(self, path=""):
        self._path = path
    def getattr(self, path):
        if type(path) != str:
            raise TypeError("arg must be str")
        return Chain("%s/%s" % (self._path, path))
    call = getattr
    def str(self):
        return self._path
print(Chain().status.user.timeline.list)
print(Chain().users("jack").repos)