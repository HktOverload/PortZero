# PortZero by HktOverload

import collections
from utils import *
from events import *
from entities import *
from geom import *
from worlds import *

Export('Scene') @ globals()

Ens = tuple[Entity, Geometry]

class Scene(object):
    __slots__ = 'name', 'entia', 'observers', 'events'
    def __init__(
        self, name: str,
        entia: list[Ens], observers: dict[str, list[Entity]],
    ):
        self.name = name
        self.entia = entia
        self.observers = observers
        self.events: t.Deque[Event] = collections.deque()

    def updateObservers(self, i: int):
        entity, _ = self.entia[i][0]
        for eventName in entity.observes():
            if eventName not in self.observers:
                self.observers[eventName] = []
            self.observers[eventName].append(entity)
    
    def tick(self):
        self.updateObservers()
        self.sendSceneEvents()
        for event in self.events:
            if event.name == '!spawn':
                self.entia.append((event.data['new-entity'], None))
            else:
                for observer in self.observers[event.name]:
                    observer.recv(event)
        for i, (entity, _) in enumerate(self.entia):
            self.events.extend(entity.sends())
            self.entia[i][1] = entity.geometry()
