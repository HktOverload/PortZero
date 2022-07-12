# PortZero by HktOverload

import abc
from lib2to3.pytree import Base
from events import *
from utils import *
from geom import *

Export(...) @ globals()

class Entity(abc.ABC):

    def observes(self) -> list[str]:
        return []

    def recv(self, event: Event) -> None:
        raise UnknownMsg(event.name)

    def sends(self) -> t.Generator[Event, None, None]:
        yield from ()

    @abc.abstractmethod
    def geometry(self) -> Geometry:
        pass

    def drawOverlay(self) -> None:
        pass

class UnknownMsg(BaseException):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'Cannot process message (with name {self.name})'

class Title(Entity):
    __slots__ = ()
    def __init__(self):
        pass

    def geometry(self):
        return []
    
    def drawOverlay(self):
        print('Welcome!')
