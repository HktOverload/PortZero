# PortZero by HktOverload

import abc
from events import *
from utils import *
from geom import *
from worlds import *

Export(...) @ globals()

class Entity(abc.ABC):

    @abc.abstractmethod
    def observes(self) -> list[str]:
        pass

    @abc.abstractmethod
    def recv(self, event: Event) -> None:
        pass

    @abc.abstractmethod
    def geometry(self) -> Geometry:
        pass
