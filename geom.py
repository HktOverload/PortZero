# PortZero by HktOverload

import typing
from utils import *

Export(...) @ globals()

class Coord2(typing.NamedTuple):
    x: float; y: float

    def __add__(self, other):
        if not isinstance(other, Coord2):
            return NotImplemented
        return Coord2(
            x = self.x + other.x,
            y = self.y + other.y,
        )

    def __rmul__(self, other):
        if not isinstance(other, float):
            return NotImplemented
        return Coord2(
            x = self.x * other,
            y = self.y * other,
        )

class Coord3(typing.NamedTuple):
    x: float; y: float; z: float

    def __add__(self, other):
        if not isinstance(other, Coord3):
            return NotImplemented
        return Coord3(
            x = self.x + other.x,
            y = self.y + other.y,
            z = self.z + other.z,
        )

    def __rmul__(self, other):
        if not isinstance(other, float):
            return NotImplemented
        return Coord3(
            x = self.x * other,
            y = self.y * other,
            z = self.z * other,
        )
    
    def dropTo2(self):
        return Coord2(x=self.x, y=self.y)

class Tri3(typing.NamedTuple):
    a: Coord3; b: Coord3; c: Coord3

class Hull(typing.NamedTuple):
    verts: list[float]
    tris: list[Tri3]

Geometry = list[Hull]

class Xform3(object):
    'TODO'
