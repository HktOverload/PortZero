# PortZero by HktOverload

import operator, random

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

"""
Tests!

First, declare a global variable tests as:
tests = []
Then, define tests using @addTest(tests)
Finally, add the segment
if __name__ == '__main__':
    [ i() for i in tests ]
"""

def addTest(tests):
    def decorator(f):
        def inner():
            failed = False
            try:
                random.seed(442)
                f()
                print(f'[OK] Test {f.__name__} passed!')
            except Exception as e:
                print(f'[FAIL] Test {f.__name__} failed:\n{e}')
                failed = True
            if failed:
                print(f'[FAIL] Running again (for stacktrace):')
                random.seed(442)
                f()
        tests.append(inner)
    return decorator

def almostEqual(a, b) -> bool:
    return abs(a - b) < (10**-5)

def assertEq(lhs, rhs = True):
    if isinstance(lhs, float) and isinstance(rhs, float):
        f = almostEqual
    else:
        f = operator.eq
    if not f(lhs, rhs):
        print(f'[FAIL] In assertEq, LHS = {lhs}')
        print(f'[FAIL] In assertEq, RHS = {rhs}')
        print(f'[FAIL] ^^^^^^^^^^^^ Compared with {f.__name__}')
        raise AssertionError
