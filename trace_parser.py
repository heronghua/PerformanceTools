#!/usr/bin/env python

class trace_parser:
    
    def __init__(self, traceFilePath):
        print('trace_parser.__init__ + traceFilePath = {}'.format(traceFilePath))
        self.traceFile = open(traceFilePath)
        self.fileHasNextLine = True
        print('trace_parser.__init__ -')
        pass

    
    def parseRecord(self):
        line = self.traceFile.readline()
        self.fileHasNextLine=(line!='')
        if self.fileHasNextLine:
            print(line)
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
