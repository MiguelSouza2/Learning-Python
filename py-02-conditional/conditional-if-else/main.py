# estrutura condicional if, elif e else

print("Cardápio de hoje:\n [1] pão com ovo\n [2] arroz com feijão\n [3] macarronada\n [4] pão com mortadelado")

choice = input("escolha um (1 a 4): ")

# incio da estrutura condicional -> se 'choice' for igual a 1
if(choice == "1"):
    print("Você escolheu pão com ovo!")
# se 'choice' for igual a 2
elif(choice == "2"):
    print("Você escolheu arroz com feijão!")
# se 'choice' for igual a 3
elif(choice == "3"):
    print("Você escolheu macarronada!")
# se 'choice' for igual a 4
elif(choice == "4"):
    print("Você escolheu pão com mortadela!")
# se não se encaixar em nenhuma das anteriores
else:
    print("Opção inválida!")




