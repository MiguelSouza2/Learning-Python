# ARRAYS EM PYTHON (LIST)

# Inicializando nossa lista de compras. Note que é necessário utilizar colchetes para manipular arrays
list = []
list2 = ["abroba", "batata", "beterraba"]

print("Vamos fazer uma lista de compras!\n")
inputChoice = input("Escolha uma opção:\n[1]Adicionar ao topo\n[2]Adicionar na lista\n[3]Mesclar com outra lista")

if inputChoice == "1":
    i = 0
    while i < 1:
        listItem = input("Digite cada um dos itens que estará no topo: \n")
        # '.insert insere o elemento na posição específicada
        list.insert(0, listItem)

        
        print("Itens na lista: ", list)
        
        moreOne = input("Tem mais algum item? (s/n)\n")
        
        if moreOne!= "s":
            print("A lista final ficou: ", list)
            i += 1
    

elif inputChoice == "2":
    i = 0
    while i < 1:
        listItem = input("Digite cada um dos itens que irá ser comprado: \n")
        
        # '.append' adiciona o item ao array
        list.append(listItem)

        
        print("Itens na lista: ", list)
        
        moreOne = input("Tem mais algum item? (s/n)\n")
        
        if moreOne!= "s":
            print("A lista final ficou: ", list)
            i += 1

elif inputChoice == "3":
    i = 0
    while i < 1:
        listItem = input("Digite cada um dos itens que irá ser comprado: \n")
        
        list.append(listItem)
        
        # '.extend' une duas listas
        list2.extend(list)
        
        print("Itens na lista: ", list2)
        
        moreOne = input("Tem mais algum item? (s/n)\n")
        
        if moreOne!= "s":
            print("A lista final ficou: ", list2)
            i += 1

else:
    print("Opção inválida!")