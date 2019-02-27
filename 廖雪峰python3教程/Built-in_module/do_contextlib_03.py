# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'它的作用就是把任意对象变为上下文对象，并支持with语句'

from contextlib import closing,contextmanager
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)


'''
closing也是一个经过@contextmanager装饰的generator,这个generator编写起来如下:
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
'''