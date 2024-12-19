# OPERADORES LÓGICOS "and" "or" "not"
# Esses operadores servem para tratar com a lógica booleana, isto é, retornam true ou false

x = 2
y = 4

# operador AND -> retorna true se ambos os operandos forem true
print(x > 0 and y > 0) # True

# operador OR -> retorna true se pelo menos um dos operandos for true
print(x > 0 or y > 0) # True

# operador NOT -> inverte o valor booleano do operando
print(not x > 0) # False

# Há também, assim como em outras linguagens, os operadores "&" e "|" e que aqui servem como operadores bit a bit, isto é, utilizam os dados de forma a tratá-los como em bits
# nota que o operador "!", em python, NÃO representa o not para operações bit a bit. Em seu lugar usa-se o "~"

a = 4 # 0100 em biinário
b = 10 # 1010 em binério

print(a & b) # vai retornar 0, pois não tem bit comum entre eles 

print(a | b) # vai retornar o corresponte ao bit 1110, ou seja, 14

                                # retona 1 caso haja um bit e 0 se não.
                                        # 0 | 1 = 1
                                        # 1 | 0 = 1
                                        # 0 | 1 = 1
                                        # 0 | 0 = 0

print(~a) # vai inverter o valor do bit de "a", ou seja 
                        # 0100 -> 1011 em binário e usando o complemento de dois, se tratando de um número negativo, correspondendo ao número -5.    
