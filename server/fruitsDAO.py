
import mysql.connector # pip install mysql-connector-python
                       # https://stackoverflow.com/questions/24272223/importerror-no-module-named-mysql-connector-using-python2, 03/12/2020

import dbconfig as cfg

# from sqlalchemy.dialects.mysql import pymysql

class FruitsDAO:
    db = ""
    def connectToBD(self):
        self.db = pymysql.connect(
            host=cfg.pymysql['host'],
            user=cfg.pymysql['user'],
            password=cfg.pymysql['password'],
            database=cfg.pymysql['database']
        )

    def __init__(self):
        self.db = mysql.connector.connect(
        host = ["localhost"],
        user = ["root"],
        password = ["rootuser"],
        database = ["datarep"]
        )
    



# https://github.com/andrewbeattycourseware/dataRepresenation2020/blob/master/code/week09-server1linktoDB.py/studentDAO.py

