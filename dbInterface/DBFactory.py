#coding=utf-8
#!/usr/bin/env python
from SQLiteDBHelper import *;
from MySQLDBHelper import *;

def Factory(dbName = "SQLiteDBHelper"):

    dataBases = {"SQLiteDBHelper":SQLiteDBHelper,
            "MySQLDBHelper":MySQLDBHelper
            }

    return dataBases[dbName]()
    
