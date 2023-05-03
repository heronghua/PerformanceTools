#coding=utf-8
#!/usr/bin/env python
import sqlite3
import LogHelper as Log

from dbInterface.BaseDBHelper import BaseDBHelper
DB_FILE_SUFFIX="db"

class SQLiteDBHelper(BaseDBHelper):
    def __init__(self):
        Log.d("+")
        super(SQLiteDBHelper, self).__init__(DB_FILE_SUFFIX)
        #do create table
        self.conn=sqlite3.connect(self.outputFilePath) 
        self.cursor=self.conn.cursor()

        table = """CREATE TABLE IF NOT EXISTS {}(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, tag VARCHAR(255), startTime NUMERIC, endTime NUMERIC);""".format(self.TABLE_NAME)
        self.cursor.execute(table)
        self.conn.commit()
        Log.d("-")
        pass


    def insertColumn(self,tag,startTime,endTime):
        Log.d("+")
        sqlInsert='''INSERT INTO PERF_T (tag,startTime,endTime) VALUES ("{}",{},{})'''.format(tag,startTime,endTime)
        #sqlInsert='''INSERT INTO PERF_T (tag,startTime,endTime) VALUES ("onShutterButtonClick",123.566,566.098)'''
        self.cursor.execute(sqlInsert)
        self.conn.commit()
        Log.d("-")
        pass

    def release(self):
        Log.d("+")
        self.cursor.close()
        self.conn.close()
        Log.d("-")
        pass
