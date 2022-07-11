# PortZero by HktOverload

import typing
from utils import *

Export(...) @ globals()

class Coord2(typing.NamedTuple):
    x: float; y: float

    def __rmul__(self, other):
        if not isinstance(other, float):
            return NotImplemented
        return Coord2(
            x = x * other,
            y = y * other,
        )

class Coord3(typing.NamedTuple):
    x: float; y: float; z: float

class Tri3(typing.NamedTuple):
    a: Coord3; b: Coord3; c: Coord3

class Hull(typing.NamedTuple):
    verts: list[float]
    tris: list[Tri3]

Geometry = list[Hull]

class Xform3(object):
    'TODO'
