from container import Container
from threading import Thread
import time

from coin_info_loader import CoinInfoLoader

class Feeder:
    _targets = []
    _is_start = False
    _thread = Thread()
    
    @classmethod
    def append(self, target):
        if not issubclass(target, Container):
            raise TypeError
        Feeder._targets.append(target)

    @classmethod
    def start(self):
        if not Feeder._is_start:
            Feeder._is_start = True
            Feeder._thread = Thread(target = Feeder._feed)
            Feeder._thread.start()

    @classmethod
    def _feed(self):
        while True:
            time.sleep(0.5)
            
            rate = CoinInfoLoader.rate()['data'][0]
            
            for target in Feeder._targets:
                target.append(rate)
