# TRABALHANDO COM CLASSES

# Uma classe é uma representação genérica de como o deveria passar, já o objeto é exatamente o tipo. Exemplo: classe "carro", objeto "Corsa Wind"; classe "fruta", objeto "Banana"

# Veja com a classe "fruta"
class Fruit:
    fruit_text = "Olá, eu sou uma fruta!"
    
    # Criando uma função "apodrecer" da classe fruta. Note que é necessário o parâmetro self como primeiro parâmetro
    def rot(self):
        print("Estou apodrecendo...")
    
# Agora instanciando os objetos "Maçã" e "Banana"
apple = Fruit()
banana = Fruit()

# Acessando uma varável própria do objeto
print(apple.fruit_text)

# Acessando um método do objeto
banana.rot()