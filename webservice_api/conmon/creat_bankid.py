#!/usr/bin/python3
# Author:xuqiao
# Time:2019/5/1212:34
# File:creat_bankid.
# Email:1462942304@qq.com
import requests

bank_abb = {
    "CCB": "中国建设银行",
    "ABC": "中国农业银行",
    "ICBC": "中国工商银行",
    "BOC": "中国银行",
    "CMBC": "中国民生银行",
    "CMB": "招商银行",
    "CIB": "兴业银行",
    "BCM": "交通银行",
    "CITICIB": "中信银行",
    "PSBC": "中国邮政银行",
}

def get_bank(cardNo):
    url = "https://ccdcapi.alipay.com/validateAndCacheCardInfo.json"
    params = {
        "_input_charset": "utf-8",
        "cardNo": cardNo,
        "cardBinCheck": "true",
    }
    try:
        bank = requests.get(url=url, params=params).json()["bank"]
    except:
        return '银行卡号输入有误！'
    if bank in bank_abb:
        return bank_abb[bank]
    else:
        return bank


print(get_bank("6228430120000000001"))


