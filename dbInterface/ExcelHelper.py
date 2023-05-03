#coding=utf-8
#!/usr/bin/env python
import openpyxl
import LogHelper as Log

from dbInterface.BaseDBHelper import BaseDBHelper

EXCEL_FILE_SUFFIX="xls"


class ExcelHelper(BaseDBHelper):
    def __init__(self):
        Log.d("+")
        super(ExcelHelper,self).__init__(EXCEL_FILE_SUFFIX)

        self.workbook=openpyxl.Workbook() 
        self.sheet=self.workbook.active
        self.sheet.title=self.TABLE_NAME
        self.workbook.save(self.outputFilePath)
        Log.d("-")
        pass


    def insertColumn(self,tag,startTime,endTime):
        Log.d("+")

        Log.d("-")
        pass

    def release(self):
        Log.d("+")
        Log.d("-")
        pass
