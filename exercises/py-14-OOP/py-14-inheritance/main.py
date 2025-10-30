# Herança dos objetos

# criando a classe pai
class human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender        
        pass

# criando a classe filho e que herda as coisas da classe pai
class worker(human):
    def __init__(self, name, age, gender, role, wage):
        super().__init__(name, age, gender)
        self.role = role
        self.wage = wage

# instanciando os objetos. Note que é necessário passar os argumentos da função pai também
test_worker = worker(name="test worker", age="18", gender="masculino", role="tester", wage=100.00)
test_worker1 = worker(name="test1", age="20", gender="feminino", role="tester1", wage=100.01)
test_worker2 = worker(name="test2", age="21", gender="masculino", role="tester2", wage=100.02)

# acessando os atributos
print(f"HUMANO: \nNOME: {test_worker.name}\nIDADE: {test_worker.age}\nGÊNERO: {test_worker.gender}\n\nFUNCIONÁRIO: \nCARGO: {test_worker.role}\nSALÁRIO: R${test_worker.wage}")
print(f"HUMANO: \nNOME: {test_worker1.name}\nIDADE: {test_worker1.age}\nGÊNERO: {test_worker1.gender}\n\nFUNCIONÁRIO: \nCARGO: {test_worker1.role}\nSALÁRIO: R${test_worker1.wage}")
print(f"HUMANO: \nNOME: {test_worker2.name}\nIDADE: {test_worker2.age}\nGÊNERO: {test_worker2.gender}\n\nFUNCIONÁRIO: \nCARGO: {test_worker2.role}\nSALÁRIO: R${test_worker2.wage}")