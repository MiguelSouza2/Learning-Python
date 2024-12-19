# estrutura condicional ternário

print("Cardápio de hoje:\n [1] pão com ovo\n [2] arroz com feijão\n [3] macarronada\n [4] pão com mortadelado")

choice = input("escolha um (1 a 4): ")

# forma compacta da estrutura de repetição if-else
print("Você escolheu pão com ovo!" if choice == "1" else "Você escolheu arroz com feijão!" if choice == "2" else "Você escolheu macarronada!" if choice == "3" else "Você escolheu pão com mortadela!" if choice == "4" else "opção inválida!")




