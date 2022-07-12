# PortZero by HktOverload

from utils import *
from scenes import *

Export('World') @ globals()

class World(object):
    # Adding __slots__ here would be kinda pointless
    def __init__(self):
        self.ports

    def titleScene(self) -> Scene:
        return Scene(
            name = 'title-screen',
            entia = [],
        )
