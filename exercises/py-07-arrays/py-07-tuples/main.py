# TUPLES

# O que é um TUPLE? Um TUPLE é um conjunto de itens guardados em uma variável 
tuple_example = ("TUPLE", 1, 'A')

# Para acessar um item dentro dele é através do índice [i]
def example():
    for i in tuple_example:
        print(f"Item: {i}")

def error_changing():
    # TUPLES são imutáveis então se tentar mudá-lo ou reordená-lo, vai falhar
    tuple_example[0] = "FALHANDO EM MUDAR"
    print(tuple_example[0])
    

def tuple_length():
    # usando o método len(), pode-se obter a quantidade de itens dentro do tuple
    print(f"Tamanho do TUPLE: {len(tuple_example)}")
    

def values_to_tuple():
    # pode-se ainda associar uma variável a um tuple
    (first, second, third) = tuple_example
    
    print(f"PRIMEIRO: {first}, TIPO: {type(first)}")
    print(f"SEGUNDO: {second}, TIPO: {type(second)}")
    print(f"TERCEIRO: {third}, TIPO: {type(third)}")
    
    # além de que pode atribuir mais de um valor a ele usando o *, sendo do tipo LIST
    
    (first, *second) = tuple_example
    
    print(f"PRIMEIRO: {first}, TIPO: {type(first)}")
    print(f"SEGUNDO: {second}, TIPO: {type(second)}")
    


values_to_tuple()