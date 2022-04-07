# !/usr/bin/env python
# -*- encoding:utf-8 -*-
import json

from flask import Flask, request, jsonify

# from lxml import html
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options  # => 引入Chrome的配置
from decryptJS import js2py_encrypt, js2py_decrypt
from service import merOrderNo

app = Flask(__name__)


# def getHtml(url, waittime=1):
#     ch_options = Options()
#     ch_options.add_argument("--headless")  # => 为Chrome配置无头模式
#     browser = webdriver.Chrome('chromedriver', )
#     browser.get(url)
#     time.sleep(waittime)
#     html = browser.page_source
#     browser.quit()
#     return html


# @app.route('/get_merOrderNo', methods=['get'])
# def get_merOrderNo():
#     # data = json.loads(request.get_data())
#     # urls = data.get('urls')
#     url = request.args.get('url')
#     data_html = getHtml(url)
#     tree = html.fromstring(data_html)
#     merOrderNo = tree.xpath('//*[@id="merOrderNo"]/text()')
#     ret = {"code": 0,
#            "msg": "",
#            "data": {
#                "oid": ""
#            }}
#     if len(merOrderNo) == 0:
#         ret["code"] = 1
#         ret["msg"] = "获取oid失败"
#     else:
#         merOrderNo = merOrderNo[0]
#         ret["data"]["oid"] = merOrderNo
#
#     return jsonify(ret)


@app.route('/get_merOrderNo', methods=['get'])
def get_merOrderNo():
    url = request.args.get('url')
    ret = merOrderNo(url)

    return jsonify(ret)


@app.route('/ExecJs', methods=['get'])
def ExecJs():
    word = request.args.get('word')
    type = request.args.get('type')
    if type == "1":
        # 1-加密
        data = js2py_encrypt(word)
        ret = {"respCode": "1000", "data": data}
    elif type == "2":
        # 2-解密
        data = js2py_decrypt(word)
        ret = {"respCode": "1000", "data": data}
    else:
        ret = {"respCode": "4001", "respMsg": "type参数错误"}

    return jsonify(ret)


@app.route('/', methods=['GET'])
def index():
    return 'hello'


if __name__ == '__main__':
    # debug=True会导致重复执行两次函数
    app.run(debug=True, port=8080)
