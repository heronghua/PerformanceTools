#coding=utf-8
#!/usr/bin/env python
from SQLiteDBHelper import *;
from MySQLDBHelper import *;
from ExcelHelper import *;

def Factory(dbName = "SQLiteDBHelper"):

    dataBases = {"SQLiteDBHelper":SQLiteDBHelper,
            "MySQLDBHelper":MySQLDBHelper,
            "ExcelHelper":ExcelHelper
            }

    return dataBases[dbName]()
    
