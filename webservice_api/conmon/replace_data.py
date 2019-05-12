#!/usr/bin/python3
# Author:xuqiao
# Time:2019/5/1111:18
# File:replace_data.
# Email:1462942304@qq.com
def replace_getdata(data,find_data,rep_data):
    if data.find(find_data) > -1:
        data = data.replace(find_data,rep_data)
    else:
        return None

    return data