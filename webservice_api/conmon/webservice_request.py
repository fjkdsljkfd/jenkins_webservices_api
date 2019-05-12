# -*- coding: utf-8 -*-#
# @Time :2019/4/1513:43
# @Author :xuqiao  
# @Email :1462942304@qq.com
# @File :webservice_request.py
from suds.client import Client
import suds
from webservice_api.conmon.read_conf import Config
from webservice_api.conmon.logger import logger
logger = logger(__name__)
class WebApi:
    def __init__(self,url):
        url = Config().getvalue("url","pre_url") + url
        self.client = Client(url)
    def info_api(self,api,data):
        logger.info("测试数据是：{}".format(data))
        if type(data) == str:
            data = eval(data)
        try:
            return eval("self.client.service.{}({})".format(api,data))
        except suds.WebFault as e:
                return e.fault.faultstring
if __name__ == '__main__':
    url = "/sms-service-war-1.0/ws/smsFacade.ws?wsdl"
    # url = "http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl"
    # client = Client(url)
    # data = {"verify_code":"100058","user_id":"张三","channel_id":"1","pwd":123456,"mobile":15511085201,"ip":"192.168.2.223"}
    # data = {"uid":"100010496","pay_pwd":"xiaoming123456","mobile":"18811085209","cre_id":"533423195210202766","user_name":"赵同出","cardid":"381525623256235622","bank_type":1001,"bank_name":"中国银行"}
    data = {"client_ip":"168.12.23","tmpl_id":"1","mobile":"18811085203"}
    res = WebApi(url).info_api("sendMCode",data)
    print(res)





