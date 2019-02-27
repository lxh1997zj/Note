# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'hhh.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):  # 方法一：
    '返回指定分数区间的名字，按分数从低到高排序'
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute('select * from user where score>=? and score<=?', (low, high))
        values = cursor.fetchall()
        values.sort(key=lambda x: x[2])
        return [i[1] for i in values]
    finally:
        cursor.close()
        conn.close()

"""
def get_score_in(low,high):  # 方法二：
    a=[]
    this_conn = sqlite3.connect(db_file)
    this_cursor = this_conn.cursor()
    for i in range(low,high+1,1):
         this_cursor.execute('select * from user where score=?',(i,))
         values=this_cursor.fetchall()
         if  values:
             a.append(values[0][1])
    this_cursor.close()
    this_conn.close()
    return a
"""

# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')