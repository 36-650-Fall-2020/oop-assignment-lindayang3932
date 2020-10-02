import sys
from abc import ABCMeta, abstractmethod
class read ():
    __metaclass__ = ABCMeta
    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def date_reformat(self):
        pass