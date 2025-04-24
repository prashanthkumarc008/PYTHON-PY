class Car:
    total_cars = 0  # Static variable to track total cars in inventory
    car_count = 0  # Static variable to track cars in the showroom

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.total_cars += 1
        Car.car_count += 1  # Increment car_count for each new car received

    def sell_car(self):
        if Car.car_count > 0:
            Car.car_count -= 1  # Decrement car_count when a car is sold
            print(f"Sold: {self.make} {self.model}")
        else:
            print("No cars to sell.")

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}")


# Creating car instances
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")
car3 = Car("Ford", "Mustang")

# Displaying car information
car1.display_info()  
car2.display_info()  
car3.display_info()

# Selling cars and updating car_count
car1.sell_car()  
car2.sell_car()  

# Printing total number of cars and cars in showroom using the static variables
print("Total cars in inventory:", Car.total_cars)  
print("Cars in showroom:", Car.car_count) 
