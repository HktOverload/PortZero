# PortZero by HktOverload

import typing
from utils import *

Export(...) @ globals()

class Coord2(typing.NamedTuple):
    x: float; y: float

class Coord3(typing.NamedTuple):
    x: float; y: float; z: float

class Tri3(typing.NamedTuple):
    a: Coord3; b: Coord3; c: Coord3

class Hull(typing.NamedTuple):
    verts: list[float]
    tris: list[Tri3]

Geometry = list[Hull]
