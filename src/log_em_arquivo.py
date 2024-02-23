from src.manipulador_de_log import ManipuladorDeLog


class LogEmArquivo(ManipuladorDeLog):
    @classmethod
    def log(cls, mensagem):
        with open('data/log.txt', 'a') as arquivo:
            arquivo.write(mensagem + '\n')
