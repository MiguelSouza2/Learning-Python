# TRABALHANDO COM CLASSES

# Uma classe é uma representação genérica de como o deveria passar, já o objeto é exatamente o tipo. Exemplo: classe "carro", objeto "Corsa Wind"; classe "fruta", objeto "Banana"

# Veja com a classe "fruta"
class Fruit:
    fruit_text = "Olá, eu sou uma fruta!"
    
    # Criando uma função "apodrecer" da classe fruta. Note que é necessário o parâmetro self como primeiro parâmetro
    def rot(self):
        print("Estou apodrecendo...")

# É possível alterar um valor de um objeto com uma função de fora do objeto
def change_object_variable(obj : object, var, new_value):
    setattr(obj, var, new_value)
    
# Agora instanciando os objetos "Maçã" e "Banana"
apple = Fruit()
banana = Fruit()

# Acessando uma varável própria do objeto
print(apple.fruit_text)

# Acessando um método do objeto
banana.rot()

change_object_variable(banana, "fruit_text", "Agora eu sou uma fruta podre... ;(")


print(banana.fruit_text)