# O que é um ambiente virtual?
Em Python, um ambiente virtual (ou virtual environment) é um espaço isolado onde você pode instalar e gerenciar pacotes e dependências sem afetar o sistema inteiro ou outros projetos.

# Como criar um ambiente virtual em Python?
Para criar um ambiente virtual em Python, primeiro você troca para a pasta onde você quer o ambiente virtual, aí basta seguir a seguinte estrutura:

```python -m venv project_name (no nosso caso é "py-15-virtual-environment")```

Irá resultar em uma estrutura de arquivos:
```
project_name
|— Include
|— Lib
|— Scripts
|— .gitignore
|— pyvenv.cfg 
```


Para ativar o ambiente virtual, basta acionar o script activate dentro de Scripts
```project_name\Scripts\activate```

Ele deve mostrar no terminal algo assim:
```○ (myfirstproject) C:\Users\...\Learning-Python\exercises\py-16-virtual-environments>```

Aí para desativar, simplesmente se usa o script 'deactivate':
```deactivate```

# Bibliotecas com o ambiente virtual
Todas as bibliotecas baixadas em um ambiente virtual estarão guardadas na pasta Lib. Seguindo o exemplo:

```pip install requests (por exemplo)```

Note que agora existe, dentro da pasta Lib, uma pasta para o requests.
```
Lib
|— site-packages
  |— ...
  |— requests
  |— requests-2.32.5.dist-info
  |— ...
```


