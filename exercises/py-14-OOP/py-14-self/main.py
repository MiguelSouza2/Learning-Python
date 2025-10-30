# PARÂMETRO self

class test:
    # note que a função __init__ vai precisar do parâmetro self para acessar o objeto instanciado
    def __init__(self):
        # Dessa forma, podemos guardar as informaç~pes dentro de uma variável do objeto
        self.test = "Hello World!"
        pass
    
    def exclusive_var(self, value):
        self.value = value
        print(f"{self.test} Esse é o valor exclusivo dessa variável: {self.value}")

# acessandos a propriedades do objeto
test1 = test()
test2 = test()
test3 = test()

test1.exclusive_var("valor exclusivo 1")
test2.exclusive_var("valor exclusivo 2")
test3.exclusive_var("valor exclusivo 2")
