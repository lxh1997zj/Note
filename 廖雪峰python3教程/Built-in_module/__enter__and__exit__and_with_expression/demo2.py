# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# 参考url = 'https://www.cnblogs.com/lipijin/p/4460487.html'

class Sample:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('type:', exc_type)
        print('value:', exc_val)
        print('trace:', exc_tb)

    def do_something(self):
        bar = 1 / 0
        return bar + 10

with Sample() as sample:
    sample.do_something()
# 在with后面的代码块抛出任何异常时，__exit__()方法被执行。正如例子所示，异常抛出时，与之关联的type，value和stack trace传给__exit__()方法，因此抛出的ZeroDivisionError异常被打印出来了。开发库时，清理资源，关闭文件等等操作，都可以放在__exit__方法当中。
