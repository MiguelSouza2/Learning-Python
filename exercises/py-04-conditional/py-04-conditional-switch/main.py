# RECOMENDO VER A AULA SOBRE FUNÇÕES ANTES DE VER AO SWITCH

#Python não tem um comando switch nativo como outras linguagens (C, Java, etc.), mas podemos simular o comportamento de um switch usando dicionários ou estruturas if-elif-else.

# estrutura condicional if, elif e else

print("Cardápio de hoje:\n [1] pão com ovo\n [2] arroz com feijão\n [3] macarronada\n [4] pão com mortadela")

choice = input("escolha um (1 a 4): ")

# Relaciona com a variável
match choice:
    # divide entre casos
    case "1":
        print("VOCÊ ESCOLHEU PÃO COM OVO")
        
    case "2":
        print("VOCÊ ESCOLHEU ARROZ COM FEIJÃO")
        
    case "3":
        print("VOCÊ ESCOLHEU MACARRONADA")
        
    case "4":
        print("VOCÊ ESCOLHEU PÃO COM MORTADELA")
        