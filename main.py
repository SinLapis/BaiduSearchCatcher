import requests, urllib, sys
__author__ = 'SinLapis'

key = '成电'
url = 'http://www.baidu.com/s?wd=' + urllib.parse.quote(key)
res = requests.get(url)
print(res.text)
# filename = 'html.txt'
# html_file = open(filename, 'w')
# html_file.write(res.text)
# html_file.close()
