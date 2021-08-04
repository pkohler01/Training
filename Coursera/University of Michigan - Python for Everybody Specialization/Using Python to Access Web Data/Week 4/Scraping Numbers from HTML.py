## Sources
# Cited Sample: https://www.py4e.com/code3/urllink2.py?PHPSESSID=63de596b1811860e65aa3b76d9c0e987
# Source file: http://py4e-data.dr-chuck.net/comments_1319581.html

## BeautifulSoup
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
import urllib

from urllib import request
from bs4 import BeautifulSoup
html = request.urlopen('http://py4e-data.dr-chuck.net/comments_1319581.html').read()
lst = list()
count = 0
soup = BeautifulSoup(html, "html.parser")
tags = soup('span')
for tag in tags:
    count = count + 1
    c = int(tag.get_text())
    lst.append(c)
print('Counted: ', count)
print('Sum: ', sum(lst))
