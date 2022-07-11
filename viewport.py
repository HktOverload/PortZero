# PortZero by HktOverload

from utils import *
from geom import *

Export(None) @ globals()

class Viewport(object):
    __slots__ = 'focalLength', 'xform'
    def __init__(self, focalLength: float, xform: Xform3):
        self.focalLength = focalLength
        self.xform = xform
    
    def map(self, vert: Coord3) -> Coord2:
        x, y, z = self.xform.apply(vert)
        if z <= 0:
            return None
        fac = self.focalLength / z
        return fac * Coord2(x=x, y=y)
