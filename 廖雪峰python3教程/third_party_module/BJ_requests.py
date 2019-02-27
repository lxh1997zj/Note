import requests
r = requests.get('https://www.douban.com/')
print(r.status_code)
# print(r.text)

# r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.url)

print(r.encoding)

# print(r.content)

# r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# print(r.json())

# r = requests.get('https://douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r.text)

# r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})

# params = {'key': 'value'}
# r = requests.post(url, json=params)

"""
url = 'https://www.douban.com'
upload_files = {'file': open('report.xlsx', 'rb')}
r = requests.post(url, files=upload_files)
"""

# r.headers={'Content-Type': 'text/html; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Content-Encoding': 'gzip'}
# print(r.headers['Content-Type'])

"""
Cookie: bid=50qHvWcB6HY; 
douban-fav-remind=1; ll="118097";
 __utma=30149280.111720098.1542601720.1550499568.1550906738.5; 
 __utmc=30149280; __utmz=30149280.1550906738.5.4.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided);
 __utmt=1;
 __utmb=30149280.1.10.1550906738
 """

print(r.cookies['bid'])
url = 'https://www.douban.com/'
cs = {'token': '12345', 'status': 'working'}
r = requests.get(url, cookies=cs)

# r = requests.get(url, timeout=2.5) # 2.5秒后超时
