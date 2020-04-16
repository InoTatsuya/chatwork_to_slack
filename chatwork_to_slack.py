import sys
import json
import requests
import time
import param

url = param.CHAT_URL + '/rooms/' + param.CHAT_ROOMID + '/messages'
headers = { 'X-ChatWorkToken': param.CHAT_APIKEY }


while 1:
    sys.stderr.write("*** 開始 ***\n")

    resp = requests.get(url,headers=headers)

    if resp.status_code == 200:
        print(resp)
        dict_data = json.loads(resp.content)
        print(dict_data)
        print(dict_data[0]['body'])
    sys.stderr.write("*** 終了 ***\n")
    time.sleep(param.INTERVAL)