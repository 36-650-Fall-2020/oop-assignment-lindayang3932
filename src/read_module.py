from abc import ABC, abstractmethod
class read (ABC):
    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def date_reformat(self):
        pass