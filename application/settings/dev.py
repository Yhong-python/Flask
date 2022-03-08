# coding=utf-8
"""
File: dev.py
Created on 2022/3/7 17:12
__author__= yangh
__remark__=
"""

from . import Config

class DevelopementConfig(Config):
    """开发模式下的配置"""
    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO= True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/students?charset=utf8"
    AUTO_CREATE_TABLE='ON'
    MYSQL_DB='students'