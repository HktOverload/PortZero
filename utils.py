# PortZero by HktOverload

"""
Exports!

For this project, the convention for imports is:
import builtin1, builtin2 # obviously optional
from utils import *
from internal import * # obviously optional

Then, they should use the Export utility to set __all__.
It works as follows:
- Export(None) @ globals() #=> exports nothing
- Export('a b') @ globals() #=> exports a and b
- Export(...) @ globals() #=> exports everything

Yes, this is a super weird way to do it.
It abides by $(python3 -c 'import this'), so I think it's fine.
Who needs PEP8 anyway?
"""

class InvalidExportIndicator(BaseException):
    def __init__(self, indicator):
        self.indicator = indicator

    def __str__(self):
        return f'''
        {self.indicator} is not valid.
        Use a space-seperated string of what to export,
        'None' for nothing, or '...' for everything.
        '''

class InvalidExportTarget(BaseException):
    def __init__(self, target):
        self.target = target

    def __str__(self):
        return f'''
        {self.target} is not a valid.
        It should be 'globals()' in the (non-utils) module.
        '''

class Export(object):
    __slots__ = 'shouldSet', 'allValue'
    def __init__(self, indicator):
        if indicator == None:
            self.shouldSet = True
            self.allValue = []
        elif indicator == ...:
            self.shouldSet = False
            self.allValue = None
        elif isinstance(indicator, str):
            self.shouldSet = True
            self.allValue = indicator.split(' ')
        else:
            raise InvalidExportIndicator(indicator)
    
    def __matmul__(self, target):
        if not isinstance(target, dict):
            raise InvalidExportTarget(target)
        if not '__name__' in target:
            raise InvalidExportTarget(target)
        if self.shouldSet:
            target['__all__'] = self.allValue
