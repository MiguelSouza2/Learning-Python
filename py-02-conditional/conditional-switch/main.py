# RECOMENDO VER A AULA SOBRE FUNÇÕES ANTES DE VER AO SWITCH

#Python não tem um comando switch nativo como outras linguagens (C, Java, etc.), mas podemos simular o comportamento de um switch usando dicionários ou estruturas if-elif-else.

# estrutura condicional if, elif e else

print("Cardápio de hoje:\n [1] pão com ovo\n [2] arroz com feijão\n [3] macarronada\n [4] pão com mortadelado")

choice = input("escolha um (1 a 4): ")

def switch_opt(choice):
    switch_choice = {
        "1" : "Você escolheu pão com ovo!",
        "2" : "Você escolheu arroz com feijão!",
        "3" : "Você escolheu macarronada!",
        "4" : "Você escolheu pão com mortadela!"
    }
    print(switch_choice.get(choice, "opção inválida"))
    
switch_opt(choice)