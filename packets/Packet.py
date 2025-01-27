from abc import ABC, abstractmethod


class Packet(ABC):
    #Abstract method used to build and pack a packet object in bytes-form.
    @abstractmethod
    def build(self):
        pass
