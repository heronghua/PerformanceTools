
#coding=utf-8
#!/usr/bin/env python
import sqlite3

class SQLiteDBHelper:
    def __init__(self):
        print("[SQLiteDBHelper.__init__]+")
        #do create table
        self.conn=sqlite3.connect("output/anylyze.db") 
        self.cursor=self.conn.cursor()

        table = """CREATE TABLE IF NOT EXISTS PERF_T(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, tag VARCHAR(255), startTime NUMERIC, endTime NUMERIC);"""
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
