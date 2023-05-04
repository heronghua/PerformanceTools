#coding=utf-8
#!/usr/bin/env python
import sys
import os
import datetime
import io

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

log = io.open(os.path.join(LOG_FILE_PATH),'a',encoding='utf8',)

@findCaller
def i(msg,caller=''):
    timeStamp=datetime.datetime.now().strftime(DATE_FORMAT)
    if LOG_LEVEL <= LOG_LEVEL_I:
        msg="{}\tINFO\t{: ^30}\t{}".format(timeStamp,caller,msg)
        print(msg)
        log.write(u'{}\n'.format(msg))
        pass
    pass

@findCaller
def d(msg,caller=''):
    timeStamp=datetime.datetime.now().strftime(DATE_FORMAT)
    if LOG_LEVEL <= LOG_LEVEL_D:
        msg="{}\tDEBUG\t{: ^30}\t{}".format(timeStamp,caller,msg)
        print(msg)
        log.write(u'{}\n'.format(msg))
        pass
    pass

@findCaller
def e(msg,caller=''):
    timeStamp=datetime.datetime.now().strftime(DATE_FORMAT)
    if LOG_LEVEL <= LOG_LEVEL_E:
        msg="{}\tERROR\t{: ^30}\t{}".format(timeStamp,caller,msg)
        print(msg)
        log.write(u'{}\n'.format(msg))
        pass
    pass

@findCaller
def w(msg,caller=''):
    timeStamp=datetime.datetime.now().strftime(DATE_FORMAT)
    if LOG_LEVEL <= LOG_LEVEL_W:
        msg="{}\tWARNING\t{: ^30}\t{}".format(timeStamp,caller,msg)
        print(msg)
        log.write(u'{}\n'.format(msg))
        pass
    pass

@findCaller
def v(msg,caller=''):
    timeStamp=datetime.datetime.now().strftime(DATE_FORMAT)
    if LOG_LEVEL <= LOG_LEVEL_V:
        msg="{}\tVERBOSE\t{: ^30}\t{}".format(timeStamp,caller,msg)
        print(msg)
        log.write(u'{}\n'.format(msg))
        pass
    pass
