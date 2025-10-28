# DICIONÁRIOS EM PYTHON

# um dicionário pode ser declarado colocando em entre chaves {}. Além disso, pode-se acessar os valores (values) pelas respectivas chaves (key), podendo os valores serem de diversos tipos
dict_example = {
    "example-1" : 1, # chave "example1", valor 1
    "example-2" : "essa é uma string em python",
    "example-3" : 3.14,
    "example-4" : 'P',
    "example-5" : ["list1", 2],
    "example-6" : {"first" : "nested dict", "second" : 2}
}

def acess_keys():
    # vai printar uma lista com todas as CHAVES (key) utilizando o método keys()
    print(dict_example.keys())
        
def acess_values():
    # vai printar uma lista com todos os valores (values) utilizando o método values()
    print(dict_example.values())

def acess_items():
    # vai printar uma lista com todos os itens (key, value) utilizando o método items()
    print(dict_example.items())

def acess_specific_item(key):
    # vamos utilizar a chave específica para mostrar um valor específico do dicionário
    print(dict_example[key])

def add_new_item(value, key):
    # vamos adicionar um novo item no dicionário
    # dict_example[key] = value
    # ou através do método update()
    dict_example.update({key : value})
    print(dict_example.values())
    print(dict_example[key])

def update_item(value, key):
    # podemos também atualizar um item dentro de um dicionário com o método update()
    dict_example.update({key : value})
    print(dict_example.values())
    print(dict_example[key])

def remove_item_by_key(key):
    # É possível remover um item específico com o método pop() ou com a keyword del
    # del dict_example[key]
    dict_example.pop(key)
    print(dict_example.values())

def remove_last_item():
    dict_example.popitem()
    print(dict_example.values())

def remove_dict(dict_name):
    # podemos apagar o dicionário todo com a keyword del também
    del dict_name
    try:
        print(f"O dicionário {dict_name} ainda existe")
    except Exception as e:
        print(f"Esse dicionário não existe ou não existe mais! Erro: {e}")
        
def clean_dict(dict_name : dict):
    # É possível limpar todos os itens e deixar o dicionário vazio apenas o redefinindo
    # dict_name = {}
    # ou utilizando o método clear()
    dict_name.clear()
    print(dict_name)
    
def copy_dict(dict_name : dict):
    # Através do método copy() ou dict(), é possível fazer uma cópia do dicionário
    print(f"ORGINAL: {dict_name}")
    print(f"CÓPIA COM COPY(): {dict_name.copy()}")
    print(f"CÓPIA COM DICT(): {dict(dict_name)}")
    
def acess_nested_dict_value(dict_name : dict, key1, key2):
    # Vamos acessar um dicionário dentro de um dicionário apenas utilizando a chave que referencia o primeiro dicionário e a que referencia o valor
    print(dict_name[key1][key2])
    
acess_nested_dict_value(dict_example, "example-6", "first")