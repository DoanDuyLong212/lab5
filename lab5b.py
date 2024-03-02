#1
class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
max_speed =input("enter max speed: ")
mileage = input("enter mileage: ")
my_vehicle = Vehicle(max_speed,mileage)
print(f"Max Speed: {my_vehicle.max_speed}")
print(f"Mileage: {my_vehicle.mileage}")

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
#2
class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def seating_capacity(self, capacity):
        return f"The {self.name}'s seating capacity is: {capacity}"

class Bus(Vehicle):
    def __init__(self, name, max_speed):
        super().__init__(name, max_speed)

    def seating_capacity(self, capacity=input("enter capicity: ")):
        return super().seating_capacity(capacity)

my_bus = Bus("School Bus", 60)
print(my_bus.seating_capacity())
#3
class Vehicle:
    color = "white"
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        print(f"{self.color} {self.name} max speed: {self.max_speed} mileage: {self.mileage}")
    def fare(self):
        return self.seating_capacity * 100
class Bus(Vehicle):
     def __init__(self, max_speed, mileage,seatint_capacity):
        super().__init__()
        self.seating_capacity = 50

     def fare(self):
        total_fare = super().fare()
        extra_charge = total_fare * 0.1
        final_amount = total_fare + extra_charge
        return final_amount

class Car(Vehicle):
    pass

print(Vehicle.color, Vehicle(input("enter name: "),input("enter max speed: "),input("enter mileage: ")))
#4
class Vehicle:
    def __init__(self,name,mileage,capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
class Bus(Vehicle):
    def __init__(self,name,mileage,capacity):
        super().__init__(name,mileage,capacity)
school_bus = Bus("school volvo",12,50)
bool(isinstance(school_bus,Vehicle))