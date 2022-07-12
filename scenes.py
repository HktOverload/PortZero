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
    
    def updateObservers(self, i: int):
        entity, _ = self.entia[i][0]
        for eventName in entity.observes():
            if eventName not in self.observers:
                self.observers[eventName] = []
            self.observers[eventName].append(entity)
    
    def tick(self, events: list[Event]):
        self.updateObservers()
        for event in events:
            for observer in self.observers[event.name]:
                observer.recv(event)
        for i, (entity, _) in enumerate(self.entia):
            self.entia[i][1] = entity.geometry()
