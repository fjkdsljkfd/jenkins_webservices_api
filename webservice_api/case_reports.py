# -*- coding: utf-8 -*-#
# @Time :2019/4/2814:41
# @Author :xuqiao  
# @Email :1462942304@qq.com
# @File :case_reports.py
import sys
import unittest
from webservice_api.conmon import cantins
sys.path.append("./") #project的根目录下
import HTMLTestRunner
discover = unittest.defaultTestLoader.discover(cantins.case_path,"test_*.py")
with open(cantins.reports_path + "/test.html","wb+") as file:
    runner = HTMLTestRunner.HTMLTestRunner( stream=file, verbosity=2, title="这是一个测试报告", description="有三个功能的测试报告")
    runner.run(discover)
