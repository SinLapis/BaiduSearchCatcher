import requests, urllib, sys
__author__ = 'SinLapis'

key = '成电'
url = 'http://baike.baidu.com/search?word=' + urllib.parse.quote(key)
headers = {'User-Agent': 'alexkh'}
res = requests.get(url, headers=headers)
filename = 'res.html'
html_file = open(filename, 'w', encoding='utf-8')
html_file.write(res.text.encode('latin1').decode('utf-8'))
html_file.close()
