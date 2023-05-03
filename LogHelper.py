#coding=utf-8
#!/usr/bin/env python
import sys
import os
import datetime

LOG_FILE_PATH="output/log"
DATE_FORMAT="%Y-%m-%d %H:%M:%S"

LOG_LEVEL_E=7
LOG_LEVEL_W=6
LOG_LEVEL_I=5
LOG_LEVEL_D=4
LOG_LEVEL_V=3

LOG_LEVEL=LOG_LEVEL_D

def findCaller(func):
    def wrapper(*args):
        fileName= sys._getframe(1).f_code.co_filename;
        funcName = sys._getframe(1).f_code.co_name;
        lineNumber = sys._getframe(1).f_lineno
        args = list(args)
        fileName=os.path.basename(fileName).replace(".py","")
        args.append('[{}.{}]'.format(fileName,funcName))
        func(*args)
    return wrapper

@findCaller
def i(msg,caller=''):
    timeStamp=datetime.datetime.now().strftime(DATE_FORMAT)
    if LOG_LEVEL <= LOG_LEVEL_I:
        print("{}\tINFO\t{: ^30}\t{}".format(timeStamp,caller,msg))
        pass
    pass

@findCaller
def d(msg,caller=''):
    timeStamp=datetime.datetime.now().strftime(DATE_FORMAT)
    if LOG_LEVEL <= LOG_LEVEL_D:
        print("{}\tDEBUG\t{: ^30}\t{}".format(timeStamp,caller,msg))
        pass
    pass

@findCaller
def e(msg,caller=''):
    timeStamp=datetime.datetime.now().strftime(DATE_FORMAT)
    if LOG_LEVEL <= LOG_LEVEL_E:
        print("{}\tERROR\t{: ^30}\t{}".format(timeStamp,caller,msg))
        pass
    pass

@findCaller
def w(msg,caller=''):
    timeStamp=datetime.datetime.now().strftime(DATE_FORMAT)
    if LOG_LEVEL <= LOG_LEVEL_W:
        print("{}\tWARNING\t{: ^30}\t{}".format(timeStamp,caller,msg))
        pass
    pass

@findCaller
def v(msg,caller=''):
    timeStamp=datetime.datetime.now().strftime(DATE_FORMAT)
    if LOG_LEVEL <= LOG_LEVEL_V:
        print("{}\tVERBOSE\t{: ^30}\t{}".format(timeStamp,caller,msg))
        pass
    pass
