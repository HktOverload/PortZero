# PortZero by HktOverload

import abc
from events import *
from utils import *
from geom import *
from worlds import *

Export(...) @ globals()

class Entity(abc.ABC):

    @abc.abstractmethod
    def rebuild(self, world: World):
        pass

    @abc.abstractmethod
    def recv(self, event: ExtEvent) -> None:
        pass

    @abc.abstractmethod
    def geometry(self) -> Geometry:
        pass
