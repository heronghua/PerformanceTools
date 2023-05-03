#coding=utf-8
#!/usr/bin/env python
import LogHelper as Log

class trace_parser:
    
    def __init__(self, traceFilePath):
        Log.d('trace_parser.__init__ + traceFilePath = {}'.format(traceFilePath))
        self.traceFile = open(traceFilePath)
        self.fileHasNextLine = True
        Log.d('trace_parser.__init__ -')
        pass

    
    def parseRecord(self):
        line = self.traceFile.readline()
        self.fileHasNextLine=(line!='')
        if self.fileHasNextLine:
            Log.d(line)
            return TraceRecord(line.replace('\n',''),123.232,232.312)
        else:
            return None
    def hasNext(self):
        pass
        return self.fileHasNextLine


    
class TraceRecord:
    def __init__(self,tag,startTime,endTime):
        self.tag=tag
        self.startTime=startTime
        self.endTime=endTime
        pass
