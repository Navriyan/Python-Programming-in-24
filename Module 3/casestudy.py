class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def __str__(self):
        return f'Vehicle type: {self.vehicle_type}'


class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def __str__(self):
        return (f'{super().__str__()}\n'
                f'Year: {self.year}\n'
                f'Make: {self.make}\n'
                f'Model: {self.model}\n'
                f'Number of doors: {self.doors}\n'
                f'Type of roof: {self.roof}')


# Function to get car details from user
def get_car_details():
    vehicle_type = "car"
    year = input("Enter the year of the car: ")
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")

    car = Automobile(vehicle_type, year, make, model, doors, roof)
    print("\nCar details:")
    print(car)


# Run the function to get car details from user and display them
get_car_details()