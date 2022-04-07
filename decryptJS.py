import execjs
import js2py
import json
import PyV8


def js_from_file(file_name):
    """
    读取js文件
    :return:
    """
    with open(file_name, 'r', encoding='UTF-8') as file:
        result = file.read()

    return result


context = js2py.EvalJs()
js_file = js_from_file('yaoyao_decrypt.js')
context.execute(js_file)


def decrypt(word):
    """
    解密
    :param word: 5m/ftdpr+nimgN7TB1ZyM8jyOYoO8UHWE5OTDuVU/CrQV8hdXZjOcs8LCEiNFdr+3ykoZN+cYkW88Sgp0Vh14qL2CNEBxdW1S6Wq9KF/ZYFmRTmNGHd9Gr/Q0kImUhxwJPcLpc1NbWl/kHN/04A6N1cQD58qh1iLSDYB2euAmGdX+mcDv86j6FXhi+F1555oDNfLv2aiTE8Uj7UZSYfuv0wke2yamqqNog0FJlARLVQhfriPC2jJQ8rfCUIUzQ1z7iSHiLsO5mlky/wWGylEKQmJ/hBQvWsKsa3ObXXuhDavDEbsGEslzCdr0Pq9SKZfbs4z5yQosZxv3kCqed2yYEVSVUl3ea3Aw3xjXySedp369WN4qCzIUR7zPfg8MVIvTSuQ4NHxhHLiKRQ5Ozo7zngoYZ9dhl5aaiOwfhIGXoWRxo/I3glLDaSie3KnUnohBfy1vNShcpk+J7/cxYV3B6H4YwOes/l7p5pThLU93meWjTiwINoxj6l5YS1N4TVHBl0tLw47zX+Ph4r0tCnUzDVP4KOTVY0rvwBTyyY/y85KldOksILb+it9PvYOdq0etqAUg9R5r/R1SIV/VxHNYOV7BQhNEZvbiKDO77osHzZEK6Z6NsyWoioy50ewFW3kxmKiqGgaOYE8iMyLZd4UUnUZlbMyK2oxfbDfh6kJgWE\\u003d
    :return:
    """
    context = execjs.compile(js_from_file('yaoyao_decrypt.js'))
    result = context.call("AES_Decrypt", word)
    return result


def encrypt(word):
    """
    加密
    :param word: canal=6c696e677869&tranDate=3230323230343035&orderNo=31323032323034303533393939343733&timestamp=31363439303936393832323339&version=1.4.6&macValue=565E6FFA231A5E248FEABEF64DDF12FE&_locale=zh_CN
    :return:
    """
    context = execjs.compile(js_from_file('yaoyao_decrypt.js'))
    result = context.call("AES_Encrypt", word)
    return result


def js2py_decrypt(word):
    # context = js2py.EvalJs()
    # context.execute(js_file)
    result = context.AES_Decrypt(word)
    return bytes(result, encoding='ISO8859_1').decode()


def js2py_encrypt(word):
    # context = js2py.EvalJs()
    # context.execute(js_file)
    result = context.AES_Encrypt(word)
    return bytes(result, encoding='ISO8859_1').decode()


def pyv8_decrypt(word):
    context = PyV8.JSContext()
    context.enter()
    context.eval(js_file)
    result = context.locals.AES_Decrypt(word)
    return result


def pyv8_encrypt(word):
    context = PyV8.JSContext()
    context.enter()
    context.eval(js_file)
    result = context.locals.AES_Encrypt(word)
    return result


if __name__ == '__main__':
    data = "5m/ftdpr+nimgN7TB1ZyM8jyOYoO8UHWE5OTDuVU/CrQV8hdXZjOcs8LCEiNFdr+3ykoZN+cYkW88Sgp0Vh14qL2CNEBxdW1S6Wq9KF/ZYFmRTmNGHd9Gr/Q0kImUhxwJPcLpc1NbWl/kHN/04A6N1cQD58qh1iLSDYB2euAmGdX+mcDv86j6FXhi+F1555oDNfLv2aiTE8Uj7UZSYfuv0wke2yamqqNog0FJlARLVQhfriPC2jJQ8rfCUIUzQ1z7iSHiLsO5mlky/wWGylEKQmJ/hBQvWsKsa3ObXXuhDavDEbsGEslzCdr0Pq9SKZfbs4z5yQosZxv3kCqed2yYEVSVUl3ea3Aw3xjXySedp369WN4qCzIUR7zPfg8MVIvTSuQ4NHxhHLiKRQ5Ozo7zngoYZ9dhl5aaiOwfhIGXoWRxo/I3glLDaSie3KnUnohBfy1vNShcpk+J7/cxYV3B6H4YwOes/l7p5pThLU93meWjTiwINoxj6l5YS1N4TVHBl0tLw47zX+Ph4r0tCnUzDVP4KOTVY0rvwBTyyY/y85KldOksILb+it9PvYOdq0etqAUg9R5r/R1SIV/VxHNYOV7BQhNEZvbiKDO77osHzZEK6Z6NsyWoioy50ewFW3kxmKiqGgaOYE8iMyLZd4UUnUZlbMyK2oxfbDfh6kJgWE\\u003d"
    # data = "canal=6c696e677869&tranDate=3230323230343035&orderNo=31323032323034303533393939343733&timestamp=31363439303936393832323339&version=1.4.6&macValue=565E6FFA231A5E248FEABEF64DDF12FE&_locale=zh_CN"
    print(pyv8_decrypt(data))
