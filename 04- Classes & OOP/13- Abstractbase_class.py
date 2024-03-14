
from abc import ABC, abstractclassmethod


# class for custom error
class InvalidOperatioError(Exception):
    pass


class Stream(ABC):  # derrived fomr ABC (abstract based class)
    def __init__(self):
        self.opended = False

    def open(self):
        if self.opended:
            raise InvalidOperatioError("Stream is already opened ...")
        self.opended = True

    def close(self):
        if not self.opended:
            raise InvalidOperatioError("Stream is already closed ...")
        self.opended = False

    @abstractclassmethod
    def read(self):
        pass


# Inheritasting Stream class
class FileStream(Stream):
    def read(self):
        print("Reading data from file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from network")


# creating instance
stream = Stream()
