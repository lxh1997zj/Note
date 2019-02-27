# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# 参考url = 'https://www.cnblogs.com/lipijin/p/4460487.html'

class Sample:
    def __enter__(self):
        print('In __enter__()')
        return 'Foo'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('In __exit__()')

def get_sample():
    return Sample()

with get_sample() as sample:
    print('sample:', sample)