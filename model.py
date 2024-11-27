import json
import re
class LogReview:
    def __init__(self,log,fn):
        self.log = log
        self.patterns = {}
        self.findings = []
        self.types = ['errors','warnings','notes','notice']
        self.get_patterns(fn)

    def review(self):
        for line in self.log:
            for t in self.types:
                if re.search(self.patterns[t],line[1]):
                    self.findings.append({'type':t,'lineno':line[0], 'line':line[1]})

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

