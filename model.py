import json
import re
import os

class LogReview:
    def __init__(self, log, patterns):
        self.log = log
        self.patterns = {}
        self.findings = []
        self.types = ['errors','warnings','notes','notice']
        self.get_patterns(patterns)

    def review(self):
        with open (self.log) as f:
            lines = f.readlines()
        os.remove(self.log)
        for i,line in enumerate(lines):
            for t in self.types:
                if re.search(self.patterns[t],line):
                    self.findings.append({'type':t,'lineno':i+1, 'line':line})

    def get_patterns(self,fn):
        with open (fn) as f:
            data=json.load(f)
            for t in self.types:
                if t=='notes':
                    self.patterns[t]=f"({'|'.join(data[t])})"
                else:
                    self.patterns[t]=data[t]

    @staticmethod
    def  display_patterns(fn):
        patterns = {}
        with open (fn) as f:
            data=json.load(f)
            for t in  ['errors', 'warnings', 'notes', 'notice']:
                if t=='notes':
                    patterns[t]=f"({'|'.join(data[t])})"
                else:
                    patterns[t]=data[t]
        return patterns

