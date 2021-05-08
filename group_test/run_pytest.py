# coding:utf-8
# !/usr/bin/python
# ========================================================
# Project: automationTest
# Creator: lilyluo
# Create time: 2021-05-05 07:40
# IDE: PyCharm
# =========================================================


import os, shutil
folder = "/Users/lilyluo/Documents/project/automationTest/group_test/report"
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))
