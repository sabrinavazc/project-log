from src.manipulador_de_log import ManipuladorDeLog


class LogEmTela(ManipuladorDeLog):
    @classmethod
    def log(cls, mensagem):
        return print(mensagem)
