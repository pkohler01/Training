## Assignment
# Find the link at position 18 (the first name is 1). Follow that link.
# Repeat this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: S

## Sources
# https://www.py4e.com/code3/urllinks.py?PHPSESSID=43d992ee9395bebee532446927330f14
# Sample: http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Actual: http://py4e-data.dr-chuck.net/known_by_Christin.html
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl
import re

## Variables
site = 'http://py4e-data.dr-chuck.net/known_by_Christin.html'
reps = 7
pos = 18
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = site

## Loop
for i in range(reps):
    html = urllib.request.urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    count = 0
    for tag in tags:
        count = count + 1
        if count > 18:
            break
        url = tag.get('href', None)
        name = tag.string
    print("Retrieving: " + name +", ", "URL: " + url)
