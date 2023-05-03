#coding=utf-8
#!/usr/bin/env python
import openpyxl

from dbInterface.BaseDBHelper import BaseDBHelper

EXCEL_FILE_SUFFIX="xls"


class ExcelHelper(BaseDBHelper):
    def __init__(self):
        print("[ExcelHelper.__init__]+")
        super(ExcelHelper,self).__init__(EXCEL_FILE_SUFFIX)

        self.workbook=openpyxl.Workbook() 
        self.sheet=self.workbook.active
        self.sheet.title=self.TABLE_NAME
        self.workbook.save(self.outputFilePath)
        print("[ExcelHelper.__init__]-")
        pass


    def insertColumn(self,tag,startTime,endTime):
        print("[ExcelHelper.insertColumn]+")

        print("[ExcelHelper.insertColumn]-")
        pass

    def release(self):
        print("[ExcelHelper.release]+")
        print("[ExcelHelper.release]-")
        pass
