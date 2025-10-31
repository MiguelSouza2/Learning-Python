# ENCAPSULAMENTO

class test_class:
    def __init__(self, test):
        # definindo a idade como um propriedade privada com o prefixo "__". Só pode ser acessada dentro da classe. Serve para aumentar a segurança
        # Aqui vamos guardar de forma segura na variável
        self.__test = test
    # criando uma função para pegar o valor dessa função de forma segura
    def get_private_property(self):
        return self.__test

# para pegar esse valor, é preciso com que seja chamada a função

obj = test_class("valor de teste")

# Pegando do jeito errado
# vai retonar um erro pois não dá pra acessá-la diretamente
# obj.__test

# por isso utilizamos a função get que fizemos anteriormente
prop = obj.get_private_property()
print(prop)