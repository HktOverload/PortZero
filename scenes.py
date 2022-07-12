# PortZero by HktOverload

from utils import *
from events import *
from entities import *
from geom import *
from worlds import *

Export('Scene') @ globals()

Ens = tuple[Entity, Geometry]

class Scene(object):
    __slots__ = 'name', 'entia', 'observers'
    def __init__(
        self, name: str,
        entia: list[Ens], observers: dict[str, list[Entity]],
    ):
        self.name = name
        self.entia = entia
        self.observers = observers
    
    def tick(self, world: World, events: list[ExtEvent]):
        for entity, _ in self.entia:
            entity.rebuild(world)
        self.sendSceneEvents()
        for event in events:
            for observer in self.observers[event.name]:
                observer.recv(event)
        self.sendSceneEvents()
        
        for i, (entity, _) in enumerate(self.entia):
            self.entia[i][1] = entity.geometry()
