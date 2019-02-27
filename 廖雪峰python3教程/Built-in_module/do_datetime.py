# !/usr/bin/env python3
# -*- coding:utf-8 -*-

from datetime import datetime,timedelta,timezone

def to_timestamp(dt_str,tz_str):
    tz = int(tz_str[3:-3])
    dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    # new_dt = dt + timedelta(hours=8-tz)     # 方法一
    new_dt = dt.replace(tzinfo=timezone(timedelta(hours=tz)))   # 方法二
    return new_dt.timestamp()

# (一)获取tz的方法:
# tz = tz_str.strip('UTC').split(':')[0]
# strip():返回移除字符串头尾指定的字符序列生成的新字符串
# split():返回分割后的字符串列表
# (二)正则表达式：       # 用()表示的就是要提取的分组（Group)
# 1.tz = re.match(r'UTC([+-]\d+):\d+',tz_str).group(1)
# 2.tz = re.match(r'^UTC([+-]\d+):00$',tz_str).group(1)
# 3.tz = re.match(r'UTC([+-]\d+)',tz_str).group(1)
# 4.tz = re.match(r'^(\w+)([+-]\d+):\d+',tz_str)group(2)

# 测试
t1 = to_timestamp('2015-6-1 08:10:30','UTC+7:00')
assert t1 == 1433121030.0, t1
t2 = to_timestamp('2015-5-31 16:10:30','UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
