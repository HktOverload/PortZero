# PortZero by HktOverload

import collections, itertools
from utils import *
from events import *
from entities import *
from geom import *

Export('Scene') @ globals()

Ens = tuple[Entity, Geometry]

class Scene(object):
    __slots__ = 'name', 'entia', 'observers', 'events'
    def __init__( self, name: str, entia: list[Ens]):
        self.name = name
        self.entia = entia
        self.observers: t.Dict[str, t.Set[Entity]] = {}
        self.events: t.Deque[Event] = collections.deque()
        for i in range(len(entia)):
            self.updateObservers(i)

    def updateObservers(self, i: int):
        entity, _ = self.entia[i][0]
        for eventName in entity.observes():
            if eventName not in self.observers:
                self.observers[eventName] = []
            self.observers[eventName].append(entity)
    
    def removeObserver(self, entity: Entity):
        for i in self.observers:
            i.remove(entity)

    def sendSceneEvents(self) -> list[Event]:
        for entity, geometry in self.entia:
            if entity in self.observers['!intersect']:
                for otherEntity, other in self.entia:
                    if intersects(geometry, other, pedantic = False):
                        self.events.append(
                            Event(
                                name = '!intersect',
                                data = {
                                    'other': otherEntity,
                                }
                            )
                        )
                        break
    
    def tick(self):
        self.sendSceneEvents()
        for i in range(len(self.entia)):
            self.entia[i][1] = None
        for event in self.events:
            if event.name == '!spawn':
                self.entia.append((event.data['new-entity'], None))
                self.updateObservers(len(self))
            elif event.name == '!die':
                self.entia.remove((event.data['target'], None))
                self.removeObserver(event.data['target'])
            else:
                for observer in self.observers[event.name]:
                    observer.recv(event)
        for i, (entity, _) in enumerate(self.entia):
            self.events.extend(entity.sends())
            self.entia[i][1] = entity.geometry()
