# PortZero by HktOverload
# TESTS

from utils import *
from geom import *

Export(...) @ globals()

tests = []

@addTest(tests)
def matmulIsComposition():
    for _ in range(1000):
        a, b, v = Xform3.rand(), Xform3.rand(), Coord3H.rand()
        assertEq((b @ a).applyH(v), a.applyH(b.applyH(v)))

if __name__ == '__main__':
    [ i() for i in tests ]
