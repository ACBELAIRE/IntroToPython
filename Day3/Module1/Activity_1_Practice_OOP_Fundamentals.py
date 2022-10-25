


class Car:
    def __init__(self, name, max_speed):
        self.name      = name
        self.max_speed = max_speed

    def start(self):
        print('Vroom!')

    def talk(self, driver):
        print(f'Hello, {driver}, I am {self.name}.')

myCar      = Car('Kitt',   180)
myOtherCar = Car('Speedy',  55)

myCar.talk('Michael')

"""
Create Driver Class
"""
class Driver:
    number_of_drivers = 0

    def __init__(self, name, age, ranking):
        self.name = name   
        self.age = age
        self.ranking = ranking
        Driver.number_of_drivers += 1

"""
Create Race Class
"""
class Race:
    def __init__(self, name, driver_limit,):
        self.name = name
        self.driver_limit = driver_limit
        self.drivers = []

    def add_driver(self, driver):
        if len(self.drivers)< self.driver_limit:
            self.drivers.append(driver)

    def get_average_ranking(self):
        sum = 0
        for driver in self.drivers:
            sum += driver.ranking

        return sum / len(self.drivers)



"""
Test Code
"""

s0 = Driver('Dale Earnhardt',   29, 100)
s1 = Driver('Lewis Hamilton',   36,  83)
s2 = Driver('Eliud Kipchoge',   36,  95)
s3 = Driver('Sebastian Vettel', 34,  76)
s4 = Driver('Ayrton Senna',     34,  99)

course = Race('Seattle 500', 4)

course.add_driver(s0)
course.add_driver(s1)
course.add_driver(s2)
course.add_driver(s3)
course.add_driver(s4)

print(course.get_average_ranking())
