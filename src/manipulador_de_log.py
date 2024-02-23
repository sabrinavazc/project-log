from abc import ABC, abstractclassmethod


class ManipuladorDeLog(ABC):
    @classmethod
    @abstractclassmethod
    def log(cls, mensagem):
        pass
