"""
def consumer():
	r = 'here'
	for i in range(3):
		n = yield r
		print(i)
c = consumer()
print(c.__next__())
print('第一次')
print(c.__next__())
print('第二次')
print(c.__next__())
print('第三次')
"""

"""
def simple_consumer():
	while True:
		print('-> start')
		x = yield
		print(x)
		print('-> received', x)

c = simple_consumer()
print(next(c))
print('------------')
print(c.send('hhh'))
"""

# def average():
# 	total = 0.0
# 	count = 0
# 	avg = None
# 	while True:
# 		num = yield avg
# 		print('send发送后的:',num)
# 		total += num
# 		count += 1
# 		avg = total / count

# ag = average()
# print(next(ag))
# print('----------------')
# print(ag.send(10))
# print('----------------')
# print(ag.send(20))
"""None
----------------
send发送后的: 10
10.0
----------------
send发送后的: 20
15.0"""


# def gen():
# 	for c in 'AB':
# 		yield c
# print(list(gen()))

# def gen_new():
# 	yield from 'AB'
# print(list(gen_new()))


# def generator_1(titles):
# 	yield titles
		
# titles = ['Python', 'Java', 'C++']
# for title in generator_1(titles):
# 	print('1:', title)
# for title in titles:
# 	print('2:', title)


import asyncio

async def Outer():
	print('in Outer')
	print('waiting for result1')
	result1 = await stage1()
	print('waiting for result2')
	result2 = await stage2()
	return (result1, result2)

# @asyncio.coroutine
async def stage1():
	print('In stage1')
	return '1'

# @asyncio.coroutine
async def stage2():
	print('In stage2')
	return '2'

loop = asyncio.get_event_loop()
loop.run_until_complete(Outer())
loop.close()

# @asyncio.coroutine
# def test():
#     n = "1"
#     return n

# async def hello():
#     print('Hello, world!')
#     r = await test()
#     print('Hello, again %s' % r)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()