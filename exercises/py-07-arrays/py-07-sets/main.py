# SETS em Python
# Similarmente aos tuples, você não consegue reordenar ou mudar valores, porém ainda pode adicionar valores
# SETS NÃO PODEM CONTER DUPLICATAS
str_test_set = {"test1", "test2", "test3"}
int_test_set = {1,2,3}
bool_test_set = {True, False}
misc_test_set = {0, "test1", 2, False, 'A'}

def show_value():
    print(f"str_test_set: {str_test_set}")
    print(f"int_test_set: {int_test_set}")
    print(f"bool_test_set: {bool_test_set}")
    print(f"misc_test_set: {misc_test_set}")

def show_specific_value(thisset : set, value):
    print(value if value in thisset else "Não contém no set!")

def data_type():
    print(f"str_test_set - TIPO {type(str_test_set)}")
    print(f"int_test_set - TIPO {type(int_test_set)}")
    print(f"bool_test_set - TIPO {type(bool_test_set)}")
    print(f"misc_test_set - TIPO {type(misc_test_set)}")

def add_value(thisset : set, value):
    # Adicionando com o método add(), mas se houver uma duplicata, não será adiconada
    print(f"SET ATUAL: {thisset}")
    thisset.add(value)
    print(f"SET DEPOIS: {thisset}")

def remove_value(thisset : set, value):
    # Subtraindo itens com o método remove() ou discard(), mas, com remove(), se o item não existir, retornará um erro, diferentemente de 
    print(f"SET ATUAL: {thisset}")
    # thisset.remove(value)
    thisset.discard(value)
    print(f"SET DEPOIS: {thisset}")

def join_sets(set1 : set, set2 : set):
    # Juntando os dois sets no set 1 com o método union() ou o operador |
    # print(set1.union(set2))
    print(set1 | set2)

# frozenset é uma versão imutável e que não pode adicionar ou subtrair elementos
x = frozenset({"test1", 2, True})


