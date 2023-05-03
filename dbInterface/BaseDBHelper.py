
#coding=utf-8
#!/usr/bin/env python
import os
import LogHelper as Log

OUTPUT_FILE_DIR="output/"
OUTPUT_FILE_PATH="output/anylyze.{}"
TABLE_NAME="PERF_T"

class BaseDBHelper(object):
    def __init__(self,suffix):
        #do create file
        if not os.path.exists(OUTPUT_FILE_DIR):
            os.makedirs(OUTPUT_FILE_DIR)
            pass
        self.outputFilePath=OUTPUT_FILE_PATH.format(suffix)
        if not os.path.exists(self.outputFilePath):
            os.system(r"touch {}".format(self.outputFilePath))
            pass
        if not os.path.exists(self.outputFilePath):
            raise Exception("output file not created!")
            pass
        self.TABLE_NAME=TABLE_NAME
        Log.i("output file {} created successfully!".format(self.outputFilePath))
        pass

    def getOutputFileSuffix(self):
        return ""
        pass
        
