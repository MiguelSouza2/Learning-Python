# MANIPULAÇÃO DE STRINGS EM PYTHON
str_py = " Essa é uma string em Python "

# # Uma string em python
# str1 = "string em python"
# print(str1)
# 
# # Uma string multiline em python
# str2 = """string
#         em
#             python"""
# print(str2)

def slice_str(): 
    # 'cortando uma string' método SLICE
    # vai apenas mostra do caracter na posição 1 até a 15. Resultado esperado: "ssa é uma stri"
    print(str_py[2:15])

def mod_string():
    # modificando uma string usando os métodos UPPER, LOWER, STRIP
    
    # método UPPER para deixar a string em maiúsculo
    print("UPPER: " + str_py.upper())
    # método LOWER para deixar a string em minúsculo
    print("lower: " + str_py.lower())
    # método STRIP para retirar espaços nas extremidades da string
    print("Strip: " + str_py.strip())

def conc_string():
    a = "Essa é uma "
    b = "string em Python"
    # concatenando duas strings
    print(a+b)

def formatting_str():
    # formatando duas strings (f-strings)
    age = 18
    text = "Meu nome é miguel"
    # a concatenaçõa de duas variáveis de valores diferentes vai resultar em erro
    # print(text + age)
    
    # por isso, ao invés de converter no mesmo tipo, podemos formatar em f-strings
    print(f"{text} e eu tenho {age} anos")
    
def escape_characters():
    # isso vai retornar erro por não ter a concatenação
    #print("Meu nome é " Miguel " e eu tenho 18 anos")
    
    # mas se usarmos caracteres de escape como (\', \\, \n, \r, \t, \b, \f, \ooo, \xhh)
    print("Meu nome é \" Miguel \" e eu tenho 18 anos")
    print("Meu nome é \' Miguel e eu tenho 18 anos")
    print("Meu nome é \n Miguel e eu tenho 18 anos")
    print("Meu nome é\rMiguel e eu tenho 18 anos")
    print("Meu nome é \t Miguel e eu tenho 18 anos")
    print("Meu nome é \b Miguel e eu tenho 18 anos")
    print("Meu nome é \f Miguel e eu tenho 18 anos")
    print("\110\145\154\154\157")
    print("\x48\x65\x6c\x6c\x6f")

# chamando a função    
escape_characters()