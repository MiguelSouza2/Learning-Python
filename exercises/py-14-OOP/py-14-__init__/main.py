# MÉTODO __INIT__

class worker:
    # a função __init__ é a primeira função que será executada quando instanciar o objeto. É muito útil para definir valores iniciais para o objeto
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role
        print("... CADASTRADO!!!\n")
        
        pass
    
    def good_morning(self):
        print(f"Bom dia, {self.name}! Boa sorte no serviço de hoje!")
        

miguel_jose = worker("Miguel José", 17, "Analista de vídeo")

miguel_jose.good_morning()