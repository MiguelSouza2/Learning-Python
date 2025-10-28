# MANEJAMENTO DE ARQUIVOS
# USE DENTRO DE: Learning-Python\exercises\py-13-file-handling

filename = "test.txt"
json_filename = "test.json"

def open_file(filename, mode):
    # Através do método open(), é possível abrir um arquivo, sendo necessário dois parâmetros: o filename e o modo em que será aberto
    # Existem 4 modos diferentes: 
    # "r": o valor padrão e significa "read" para ler o arquivo
    # "w": para escrever um valor no arquivo, criando o se não existir
    # "a": para adicionar um arquivo, criando o se não existir
    # "x": cria o arquivo e retorna erro se não existir
    
    # Adicionalmente, você também pode adicionar no modo:
    # "t": para especificar como text, o que vem por padrão
    # "b": para especificar como binário
    
    f = open(filename, mode)
    
    print(f"Você escolheu READ" if mode == "r" else "Você escolheu WRITE" if mode=="w" else "Você escolheu APPEND" if mode=="a" else "Você escolheu CREATE" if mode=="x" else "Você não escolheu nenhuma opção válida!")

    return f


def read_file(f):
    # Aqui, através do método read(), podemos ler o arquivo como texto, possibilitando o print na tela
    print(f.read())
    

def with_read_file(f):
    # também pode-se fazer essa leitura com o WITH
    with f:
        print(f.read())


def write_file(f):
    # O método write() vai servir para escrever naquele arquivo 
    with f:
        # O método write vai sobrescrever o conteúdo 
        f.write("Novo conteúdo do texto!")

def append_file(f):
    # Similarmente ao write em que sobrescrevemos por estarmos no modo "w", aqui no append o modo é o "a" para adicionarmos o texto no final do arquivo
    with f:
        f.write("\nConteúdo adicionado\n")

# with_read_file(open_file(json_filename, "r"))
# with_read_file(open_file(filename, "r"))