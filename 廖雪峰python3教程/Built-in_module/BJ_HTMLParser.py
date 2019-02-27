from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print('<%s>' % tag)

	def handle_endtag(self, tag):
		print('</%s>' % tag)

	def handle_startendtag(self, tag, attrs):
		print('<%s/>' % tag)

	def handle_data(self, data):
		print(data)

	def handle_comment(self, data):
		print('<!--', data, '-->')

	def handle_entityref(self, name):
		print('&%s:' % name)

	def handle_charref(self, name):
		print('&#%s:' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

"""
handle_startendtag  处理开始标签和结束标签
handle_starttag     处理开始标签，比如<xx>
handle_endtag       处理结束标签，比如</xx>
handle_charref      处理特殊字符串，就是以&#开头的，一般是内码表示的字符
handle_entityref    处理一些特殊字符，以&开头的，比如  
handle_data         处理数据，就是<xx>data</xx>中间的那些数据
handle_comment      处理注释
handle_decl         处理<!开头的，比如<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
handle_pi           处理形如<?instruction>的东西
"""