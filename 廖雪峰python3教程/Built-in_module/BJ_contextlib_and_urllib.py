"""
# contextlib
from contextlib import contextmanager

class Query(object):
	def __init__(self, name):
		self.name = name

	def query(self):
		print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
	print('Begin')
	q = Query(name)
	yield q
	print('End')

with create_query('Bob') as  q:
	q.query()

print('-----------------------------------------------------------')

@contextmanager
def tag(name):
	print('<%s>' % name)
	yield
	print("</%s>" % name)

with tag('h1'):
	print('hello')
	print('world')


print('-----------------------------------------------------------')

from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.baidu.com')) as page:
	for line in page:
		print(line)

# closing这个generator类似于下面这个程序
@contextmanager
def closing(thing):
	try:
		yield thing
	finally:
		thing.close()

print('-----------------------------------------------------------')
"""


# urllib
from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
	data = f.read()
	print('Status:', f.status, f.reason)
	for k, v in f.getheaders():
		print('%s: %s' % (k, v))
	print('Data:', data.decode('utf-8'))

print('-----------------------------------------------------------')

from urllib import request

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
	print('Status:', f.status, f.reason)
	for k, v in f.getheaders():
		print('%s: %s' % (k, v))
	print('Data:', f.read().decode('utf-8'))