# PortZero by HktOverload

from utils import *

Export(...) @ globals()

class Event(t.NamedTuple):
    name: str
    data: dict[str, t.Any]
    isSceneEvent: bool = False
