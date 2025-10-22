# TRATAMENTO DE ERRO COM TRY EXCEPT

def with_error():
    # vai retornar erro por não ter a variável 'invalid_string' definida
    # print(invalid_string)
    
    try:
        print(invalid_string)
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        # note que, ao invés de quebrar o código, ele vai cair no tratamento do erro
        print("Para que esse erro não se repita, defina a variável antes!!!")
        

def without_error():
    valid_string = "essa é uma string em Python"
    try:
        # Perceba que agora a variável está definida, por isso não há erro. Nesse caso, o todo o bloco TRY será executado sem cair no EXCEPT 
        print(valid_string)
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    