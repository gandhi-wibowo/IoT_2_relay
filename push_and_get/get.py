import urllib2
import json
from subprocess import call

url = "https://api.thingspeak.com/channels/111680/feeds.json"

def get_data():

    data = urllib2.urlopen(url).read()
    js = json.loads(data)
    d = js[u'feeds']
    lst = d[-1]
    if lst[u'field1'] == u'0' :
        ##field1 nilainya 0 / off run turnoff7.sh
        call(["sh","off7.sh"])
    else :
        call(["sh","on7.sh"])
        ##field1 nilainya 1 / on run turnon7.sh
    if lst[u'field2'] == u'0' :
        call(["sh","off29.sh"])
        ##field 2 nilainya 0 / run turnoff29.sh
    else :
        call(["sh","on29.sh"])
        ##field 2 nilainya 1 / run turnon29.sh



if __name__ == '__main__':
    while True:
        get_data()
