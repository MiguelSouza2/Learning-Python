# ARRAYS EM PYTHON

# Inicializando nossa lista de compras. Note que é necessário utilizar colchetes para manipular arrays
list = []

print("Vamos fazer uma lista de compras!\n")

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

