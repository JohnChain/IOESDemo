#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests
import json
import traceback
from utils import *
import threading
import time

default_headers = {'content-type': "application/json"}
class HttpOps:
    def doPost(self, url, body, header=default_headers):
        if not GLOBAL_FLAG_SELF_CHECK[0]:
            response = requests.post(url, data=json.dumps(body), headers=header)
            return response.status_code, response.text
        else:
            t = threading.currentThread()

            filetime = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
            fileName = "tid%d_%s.json" %(t.ident, filetime)
            json_str = json.dumps(body, indent=4)
            with open(fileName, 'w+') as json_file:
                json_file.write(json_str)
            time.sleep(1)
            return 200, "{}"
    def post(self, url, body):
        try:
            status_code, jsonStr = self.doPost(url, body)
        except (requests.exceptions.ReadTimeout, ConnectionError, json.JSONDecodeError):
            return "Error: 已连到主机，但接收回复超时"
        except:
            traceback.print_exc()
            return "Error: 目标主机找不到 或 端口被拒绝访问"
        if status_code == 200:
            return jsonStr
        else:
            return ("Error: code: %d, msg: %s" %(status_code, jsonStr))

if __name__ == '__main__':
    url = "http://192.168.1.222:11500/images/recog"
    if len(sys.argv) < 2:
        exit()
    httpOps = HttpOps()
    fileName = sys.argv[1]

    output = {"Face": 1, "SubClass": 1}
    imageList = {"ImageID": "changanqiche"}
    imageList["Data"] = fileBase64(fileName)
    mdir = {"Output": output, "ImageList": [imageList]}

    print("%s" %(httpOps.post(url, mdir)))
