## Sources
# Reference: http://www.py4e.com/code3/geoxml.py
# Sample: http://py4e-data.dr-chuck.net/comments_42.xml
# Actual: http://py4e-data.dr-chuck.net/comments_1319583.xml
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

## Variables
site = 'http://py4e-data.dr-chuck.net/comments_1319583.xml'



url = input("Enter XML URL: ")
if len(url) < 1:
    url = site
print("Retrieving " + site + "...")
xml = urllib.request.urlopen(url).read()
print("XML retrieved from " + url)
print(str(len(xml)) + " characters retrieved from " + url)
tree = ET.fromstring(xml)
counts = tree.findall('.//count')
print("Count: " + str(len(counts)))
vol = 0
for count in counts:
    vol += int(count.text)
print("Sum: " + str(vol))
