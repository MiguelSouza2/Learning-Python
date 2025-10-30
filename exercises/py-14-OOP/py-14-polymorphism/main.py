# POLIMORFISMO

# conceito da POO que permite que um mesmo método, função ou objeto possa ter múltiplas formas de comportamento. 

class vehicle:
    # criando uma função para a movimentação
    def move(self):
        print("Movendo...")
        
class car(vehicle):
    # sobrescrevendo a função (OVERRIDE) para que assuma uma nova forma
    def move(self):
        print("VRUMMMMM")

test_vehicle = vehicle()
test_car = car()

test_vehicle.move()
test_car.move()