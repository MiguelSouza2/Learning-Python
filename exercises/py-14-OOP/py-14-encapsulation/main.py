# ENCAPSULAMENTO

class test_class:
    def __init__(self, test):
        # definindo a idade como um propriedade privada com o prefixo "__". Só pode ser acessada dentro da classe. Serve para aumentar a segurança
        self.__test = test
    
    def get_private_property(self):
        return self.__test
    

