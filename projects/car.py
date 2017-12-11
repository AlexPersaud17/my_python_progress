# Testing the Car class
import random
# You should not change the provided class Car.
class Car:
    def __init__(self, year_model, make):
        self.year_model = year_model;
        self.make = make
        self.speed = 0
        
    def accelerate(self):
        self.speed += 5
        
    def brake(self):
        self.speed -=5
        


def main():
    # Create an instance of Car.
    my_car = Car('2008', 'Honda Accord')

    # edit the format arguments in the following line to print the info for my_car
    print("Model:{}, year:{}".format(my_car.make, my_car.year_model))
    
    print('car is accelerating: ')
    # add code here to accelerate 5 times
    # call the accelerate() method for the object my_car
    for i in range(5):
        my_car.accelerate()
    
    print ('Current speed: ', my_car.speed)
    print()
    
    print ('car is braking: ')
    # add code to brake 3 times 
    for i in range(3):
        my_car.brake()

    print ('Current speed: ', my_car.speed)

    # PART 2
    #print("This is the second car:")
    # create a second car using variable your_car
    # ask the user for the model and the year of the car (see sample output)
    # print the info in the same format you did above (for my_car)
    # You should accelerate for a random number of times (use randint(1,25))
    # Print the current speed of your_car.

    your_make = input("Enter the make of the car: ")
    your_year = input("Enter the year of this model: ")
    your_car = Car(your_make, your_year)

    print("car is accelerating...")
    for i in range(random.randint(1, 25)):
        your_car.accelerate()

    print("Current speed:", your_car.speed)


main()

