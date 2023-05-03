
#coding=utf-8
#!/usr/bin/env python
import sqlite3

from dbInterface.BaseDBHelper import BaseDBHelper
DB_FILE_SUFFIX="db"

class SQLiteDBHelper(BaseDBHelper):
    def __init__(self):
        print("[SQLiteDBHelper.__init__]+")
        super(SQLiteDBHelper, self).__init__(DB_FILE_SUFFIX)
        #do create table
        self.conn=sqlite3.connect(self.outputFilePath) 
        self.cursor=self.conn.cursor()

        table = """CREATE TABLE IF NOT EXISTS {}(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, tag VARCHAR(255), startTime NUMERIC, endTime NUMERIC);""".format(self.TABLE_NAME)
        self.cursor.execute(table)
        self.conn.commit()
        print("[SQLiteDBHelper.__init__]-")
        pass


    def insertColumn(self,tag,startTime,endTime):
        print("[SQLiteDBHelper.insertColumn]+")
        sqlInsert='''INSERT INTO PERF_T (tag,startTime,endTime) VALUES ("{}",{},{})'''.format(tag,startTime,endTime)
        #sqlInsert='''INSERT INTO PERF_T (tag,startTime,endTime) VALUES ("onShutterButtonClick",123.566,566.098)'''
        self.cursor.execute(sqlInsert)
        self.conn.commit()
        print("[SQLiteDBHelper.insertColumn]-")
        pass

    def release(self):
        print("[SQLiteDBHelper.release]+")
        self.cursor.close()
        self.conn.close()
        print("[SQLiteDBHelper.release]+")
        pass
