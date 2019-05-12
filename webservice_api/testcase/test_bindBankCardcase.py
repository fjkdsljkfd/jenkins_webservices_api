from webservice_api.conmon.logger import logger
from webservice_api.conmon import cantins
from webservice_api.conmon.random_carid import RandomCarid
from webservice_api.conmon.do_pymysql import DoMysql
from webservice_api.conmon.read_write_excel import ExcelTest
from webservice_api.conmon.context import *
from webservice_api.conmon.webservice_request import WebApi
from webservice_api.conmon.random_name import random_name
from webservice_api.conmon.random_phone import create_phone
logger = logger(__name__)
from ddt import ddt,data,unpack
import unittest
@ddt
class Bankcard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.phone = create_phone()
        logger.info("测试前的前置工作")
    @data(*ExcelTest(cantins.data_path,"bindBankCard").read_excel())
    def test_bankcard(self,case):
        logger.info("开始执行:{}".format(case.title))
        logger.info("--------------------")
        case.data = replace_getdata(case.data, "mobile_phone", self.phone)
        info_name = random_name()
        case.data = replace_getdata(case.data, "info_name", info_name)
        case.data = replace_getdata(case.data, "true_username", info_name)
        case.data = replace_getdata(case.data, "card_number", RandomCarid().gennerator())
        case.data = getdata(case.data)
        logger.info("测试的数据是：{}".format(case.data))
        logger.info("替换后的数据为：{}".format(case.data))
        res = WebApi(case.url).info_api(case.api,case.data)
        logger.info("请求接口后得到的数据：{}".format(res))
        try:
            self.assertEqual(case.exp,res["retInfo"])
            ExcelTest(cantins.data_path, "bindBankCard").write_excel(case.case_id+1,str(res["retInfo"]),"pass")
            if case.title == "正常获得验证码":
                data = DoMysql().fecth_one(eval(case.sql)["sql"])
                setattr(Code,"verify_code",data["Fverify_code"])
            if case.title == "注册成功":
                case.sql = replace_getdata(case.sql, "info_name", info_name)
                data = DoMysql().fecth_one(eval(case.sql)["sql"])
                setattr(Code,"uid",data["Fuid"])
            if case.title == "身份认证通过" and res["retInfo"] == "ok":
                if case.sql:
                    case.sql = getdata(case.sql)
                    data = DoMysql().fecth_one(eval(case.sql)["sql"])
                    setattr(Code,"futrue_name",data["Ftrue_name"])
                    setattr(Code,"car_id",data["Fcre_id"])
        except AssertionError as e:
            ExcelTest(cantins.data_path, "bindBankCard").write_excel(case.case_id + 1, str(res["retInfo"]),"failed")
            logger.error("报错了：{}".format(e))
            raise e
        logger.info("{}用例执行完成".format(case.title))
    @classmethod
    def tearDownClass(cls):
        logger.info("用例执行结束的后置工作")

