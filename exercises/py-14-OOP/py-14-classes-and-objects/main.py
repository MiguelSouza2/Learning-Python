# TRABALHANDO COM CLASSES

# Uma classe é uma representação genérica de como o deveria passar, já o objeto é exatamente o tipo. Exemplo: classe "carro", objeto "Corsa Wind"; classe "fruta", objeto "Banana"

# Veja com a classe "fruta"
class Fruit:
    def bite():
        print("YUMMY!")

# Agora instanciando o objeto "Maçã"
apple = Fruit()

# Chamando uma função do objeto
apple.bite()