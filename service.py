import binascii
import requests
import json

from decryptJS import encrypt, decrypt,js2py_decrypt,js2py_encrypt


def str2hex(s):
    """
    将字符串转成16进制
    :param s:
    :return:
    """
    return bytes.decode(binascii.hexlify(str.encode(s)))


def get_param(param):
    ret = ""
    # param = "tranDate=20220405&orderNo=1202204053999473&timestamp=1649096982239&version=1.4.6&macValue=565E6FFA231A5E248FEABEF64DDF12FE&canal=lingxi"
    for i in param.split("&"):
        j = i.split("=")
        if j[0] in ["canal", "tranDate", "orderNo", "timestamp"]:
            ret += j[0] + "="
            ret += str2hex(j[1])
        else:
            ret += j[0] + "="
            ret += j[1]
        ret += "&"
    ret += "_locale=zh_CN"
    return ret


def send_post(url, param):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
    }
    data = {"requestType": "h5",
            "cipherH5": param}
    ret = requests.post(url, data=data, headers=headers)
    return ret.json()


def merOrderNo(url_param):
    """

    :param url:https://yaoyao.cebbank.com/LifePayment/webApp/cashier/index.html?tranDate=20220405&orderNo=1202204053999473&timestamp=1649096982239&version=1.4.6&macValue=565E6FFA231A5E248FEABEF64DDF12FE&canal=lingxi
    :return:
    """
    url = "https://yaoyao.cebbank.com/LifePayment/showCashier.json"
    param = str(url_param).split("?")[1]
    param = get_param(param)
    param = js2py_encrypt(param)
    response = send_post(url, param)
    cipherModel = json.loads(response["cashierModel"])["cipherModel"]
    cipherModel = json.loads(js2py_decrypt(cipherModel))
    return cipherModel


if __name__ == '__main__':
    "canal=6c696e677869&tranDate=3230323230343035&orderNo=31323032323034303533393939343733&timestamp=31363439303936393832323339&version=1.4.6&macValue=565E6FFA231A5E248FEABEF64DDF12FE&_locale=zh_CN"
    param = "tranDate=20220405&orderNo=1202204053999473&timestamp=1649096982239&version=1.4.6&macValue=565E6FFA231A5E248FEABEF64DDF12FE&canal=lingxi"
    url = "https://yaoyao.cebbank.com/LifePayment/webApp/cashier/index.html?tranDate=20220405&orderNo=1202204053999473&timestamp=1649096982239&version=1.4.6&macValue=565E6FFA231A5E248FEABEF64DDF12FE&canal=lingxi"
    print(merOrderNo(param))
