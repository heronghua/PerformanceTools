#coding=utf-8
#================================================================
# File Name: PerformanceCalculator.py
# Author: He Ronghua
# mail: heronghua1989@126.com
# Created Time: 2023年04月30日 星期日 15时24分52秒
#================================================================
#!/usr/bin/env python
from dbInterface import Factory
from trace_parser import trace_parser
import LogHelper as Log


if __name__ == "__main__":

   Log.i("+")
   # DB factory
   factory= Factory("ExcelHelper")
   trace_parser = trace_parser("testFile")

   while trace_parser.hasNext():
       traceRecord=trace_parser.parseRecord()
       if traceRecord != None:
           factory.insertColumn(traceRecord.tag,traceRecord.startTime,traceRecord.endTime)
           pass
       pass
       
   factory.release()
   Log.i("-")
   pass

