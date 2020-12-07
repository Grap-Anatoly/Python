class DrivableInterface:
    
    def accelerate():
        print("Accelerated")
        condition = "running"
        return condition 
    def brake():
        print("Braked")
        condition = "Stopped"
        return condition
    def turn(wheels):
        if wheels == True:
            print("Turned")
        else:
            print("No wheels? Then it`s a Boat! And it`s also turned.")

class Vehicle(DrivableInterface):

    condition = "disabled"

    def __init__(self,condition,wheelsPresent,gas):
        self.condition = condition
        self.wheelsPresent = wheelsPresent
        self.gas = gas
        
    def _engine(condition):
        print("Engine is", condition)
        
    def _wheels(wheelsPresent):
        if wheelsPresent == True:
            return True
        else:
            return False
            
    def _gasTank(gas):
        print("Tank filled with", gas , "percents of gas")
    
    _engine(condition)
    
class Boat(Vehicle):
    wheels = False
    gas = 85
    print("-----Boat")
    
    Vehicle._gasTank(gas)

    condition = DrivableInterface.accelerate()
    Vehicle._engine(condition)
    
    wheels = Vehicle._wheels(wheels)
    DrivableInterface.turn(wheels)
        
    condition = DrivableInterface.brake()
    Vehicle._engine(condition)
    
class Car(Vehicle):
    wheels = True
    gas = 100
    print("-----Car")

    Vehicle._gasTank(gas)

    condition = DrivableInterface.accelerate()
    Vehicle._engine(condition)
    
    wheels = Vehicle._wheels(wheels)
    DrivableInterface.turn(wheels)
    
    condition = DrivableInterface.brake()
    Vehicle._engine(condition)
    
class SolarCar(Car):
    wheels = True
    gas = "Infinite"
    print("-----SolarCar")
    
    Vehicle._gasTank(gas)
    
    condition = DrivableInterface.accelerate()
    Vehicle._engine(condition)
    
    wheels = Vehicle._wheels(wheels)
    DrivableInterface.turn(wheels)
        
    condition = DrivableInterface.brake()
    Vehicle._engine(condition)
