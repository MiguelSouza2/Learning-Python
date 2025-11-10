import re
# O módulo re contem 4 métodos:
# findall() -> encontra todas as correspondências e retorna uma lista
# search() -> encontra as correspondências e retorna um objeto 'Match', um objeto referente à pesquisa e procura, ou 'None' se não houverem correspondências
# split() -> reparte o texto em elementos de uma lista conforme o parâmetro e a retorna
# sub() -> divide o texto e substituir uma parte por outra


test_txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse viverra."

def txt_findAll(txt):
    x = re.findall("viverra.", txt)
    return x

def txt_search(txt):
    x = re.search("ipsum", txt)
    return x

def txt_split(txt):
    x = re.split(" ", txt)
    return x

def txt_sub(txt):
    x = re.sub(" ", " - ", txt)
    return x

y = txt_findAll(test_txt)

print(y)

