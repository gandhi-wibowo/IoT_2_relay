#/usr/bin/python

import httplib, urllib
import sys

field1 = sys.argv[1]
field2 = sys.argv[2]

params = urllib.urlencode({'field1':field1,'field2':field2,'key':'API_KEY_WRITE'})
headers = {"Content-type": "application/x-www-form-urlencoded","Accept":"text/plain"}
conn = httplib.HTTPConnection("api.thingspeak.com:80")
conn.request("POST", "/update", params, headers)
response = conn.getresponse()
data = response.read()
print data
