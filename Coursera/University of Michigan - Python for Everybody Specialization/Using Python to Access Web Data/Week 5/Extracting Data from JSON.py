## Assignment
# In this assignment you will write a Python program somewhat similar to
# http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read
# the JSON data from that URL using urllib and then parse and extract the
# comment counts from the JSON data, compute the sum of the numbers in the
# file and enter the sum below

## Sources
# Reference: https://www.py4e.com/code3/json2.py?PHPSESSID=7f1c19ca4c716a04a8ad1f0d4edb2998
# Sample: http://py4e-data.dr-chuck.net/comments_42.json
# Actual: http://py4e-data.dr-chuck.net/comments_1319584.json
import json
import urllib.request, urllib.parse, urllib.error

## Variables
site = 'http://py4e-data.dr-chuck.net/comments_1319584.json'
count = 0

url = input("Enter XML URL: ")
if len(url) < 1:
    url = site
print("Retrieving " + site + "...")
payload = urllib.request.urlopen(url).read()
print("JSON retrieved from " + url)
print(str(len(payload)) + " characters retrieved from " + url)

data = json.loads(payload)
print("Data loaded...")
for item in data["comments"]:
    num = int(item['count'])
    count = count + num
print("Sum: " + str(count))
