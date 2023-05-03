
#coding=utf-8
#!/usr/bin/env python
import xlrd
import os

OUTPUT_FILE_DIR="output/"
OUTPUT_FILE_PATH="output/anylyze.{}"
TABLE_NAME="PERF_T"

class BaseDBHelper(object):
    def __init__(self,suffix):
        print("[BaseDBHelper.__init__]+")
        #do create file
        if not os.path.exists(OUTPUT_FILE_DIR):
            os.makedirs(OUTPUT_FILE_DIR)
            pass
        self.outputFilePath=OUTPUT_FILE_PATH.format(suffix)
        if not os.path.exists(self.outputFilePath):
            os.system(r"touch {}".format(self.outputFilePath))
            pass
        self.TABLE_NAME=TABLE_NAME
        print("[BaseDBHelper.__init__]-")
        pass

    def getOutputFileSuffix(self):
        return ""
        pass
        
