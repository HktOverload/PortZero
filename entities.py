# PortZero by HktOverload

import abc
from utils import *
from geom import *

Export('Entity') @ globals()

class Entity(abc.ABC):

    @abc.abstractmethod
    def geometry() -> Geometry:
        pass
