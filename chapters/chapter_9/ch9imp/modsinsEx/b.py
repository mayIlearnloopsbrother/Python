#!/usr/bin/python3

from c import Car
from a  import ElectricCar

my_car = Car('Vauxhall', 'Corsa', 2007)
print(my_car.get_descriptive_name())

my_new_car = ElectricCar('tesla', 'roadster', 2016)
print(my_new_car.get_descriptive_name())

