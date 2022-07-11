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
    
    def dropTo2(self) -> Coord2:
        return Coord2(x=self.x, y=self.y)

    def toH(self):
        return Coord3H(
            x=self.x,
            y=self.y,
            z=self.z,
            w = 1,
        )

class Tri2(typing.NamedTuple):
    a: Coord2; b: Coord2; c: Coord2

    def mapVerts(self, fn: typing.Callable[[Coord2], Coord2]):
        return Tri2(
            a = fn(self.a),
            b = fn(self.b),
            c = fn(self.c),
        )

class Tri3(typing.NamedTuple):
    a: Coord3; b: Coord3; c: Coord3

    def mapVerts(self, fn: typing.Callable[[Coord3], Coord3]):
        return Tri3(
            a = fn(self.a),
            b = fn(self.b),
            c = fn(self.c),
        )
    
    def mapTo2(self, fn: typing.Callable[[Coord3], Coord2]):
        return Tri2(
            a = fn(self.a),
            b = fn(self.b),
            c = fn(self.c),
        )

    def dropTo2(self):
        return self.mapTo2(lambda x: x.dropTo2())

class Hull(typing.NamedTuple):
    verts: list[float]
    tris: list[Tri3]

Geometry = list[Hull]

class Coord3H(typing.NamedTuple):
    x: float; y: float; z: float; w: float

    def __add__(self, other):
        if not isinstance(other, Coord3H):
            return NotImplemented
        return Coord3H(
            x = self.x + other.x,
            y = self.y + other.y,
            z = self.z + other.z,
            w = self.w + other.w,
        )

    def __rmul__(self, other):
        if not isinstance(other, float):
            return NotImplemented
        return Coord3H(
            x = self.x * other,
            y = self.y * other,
            z = self.z * other,
            w = self.w * other,
        )
    
    def pd(self):
        return Coord3(
            x = self.x / self.w,
            y = self.y / self.w,
            z = self.z / self.w,
        )

class Xform3(typing.NamedTuple):
    # Columns
    a: Coord3H; b: Coord3H; c: Coord3H; d: Coord3H

    def applyH(self, c: Coord3H):
        m = self
        return ( 0.0
            + (c.x * m.a)
            + (c.y * m.b)
            + (c.z * m.c)
            + (c.w * m.d)
        )
    
    def apply(self, c: Coord3):
        return self.applyH(
            c.toH()
        ).pd()
