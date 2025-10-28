# ITERADORES EM PYTHON

# Todos os seguintes podem ser iterados.
test_str = "test0"
test_tuple = ("test1", "test2", "test3")
test_list = ["test4", "test5", "test6"]
test_set = {"test7", "test8", "test9"}
test_dict = {
    "test10" : test_str,
    "test11" : test_tuple,
    "test12" : test_list,
    "test13" : test_set
}

def iter_items_in_range(item, r):
    # iterando cada item dentro do alcance. Note que se você colocar um range maior do que o existente ele retornará um erro
    # definindo o iterador com o método iter() 
    iterator = iter(item)
    for i in range(r):
        print(next(iterator))

def iter_all_items(item):
    iterator = iter(item)
    for i in item:
        print(next(iterator))


iter_all_items(test_str)