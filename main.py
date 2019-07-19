from feeder import Feeder
from memory_container import MemoryContainer
import time

if __name__ == "__main__":
    Feeder.append(MemoryContainer)
    Feeder.start()
    while True:
        time.sleep(1)
        print(MemoryContainer.get_data())
