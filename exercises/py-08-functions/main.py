# FUNÇÕES EM PYTHON

n1 : int = int(input("Qual o primeiro número que será somado?\n"))
n2 : int = int(input("Qual o segundo número que será somado?\n"))

# declarando a função somarNumero com os parâmetros (x e y)
def somarNumero(x : int, y : int):
    # retorna um valor int de x + y
    return x + y

# chamando a função com os parâmetros (n1 e n2) e, como o valor é do tipo inteiro, convertemos para string 
print("A soma dos dois números é de: " + str(somarNumero(n1, n2)))
