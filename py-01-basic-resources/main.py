# métodos básicos de entrada e saída e tipos de dados: str, int, float e complex

# input recebe os dados do prompt e está guardando em uma variável 'name'do tipo str -> armazena números e caracteres 
name : str = input("Please enter your name: ")

# print está mostrando na tela uma mensagem
print("seu nome é: " + name  + "!\n")
# input recebe os dados do prompt e está guardando em uma variável 'age'do tipo int -> armazena números inteiros
age : int = int(input("Please enter your age: "))

print("sua idade é de: " + age + "anos!\n")
#input recebe os dados do prompt e está guardando em uma variável 'name'do tipo float -> armazena número decimais
weight : float = float(input("Please enter your weight(kg): "))

print("seu peso é: " + weight + "kg!\n")


# o tipo complex é um pouco mais complicado pois abrange o campo da matemática dos números complexos. Aqui vai um exemplo simples:

x : complex = 2 + 3j; 

print(f"o número complexo é: {x} + !\n") 

print(f"a parte imaginária é {x.imag}") #3 é a parte imaginária

print(f"a parte real é: {x.real}") # 2 é a parte real


