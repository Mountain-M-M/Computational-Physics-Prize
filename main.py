# Importing Files


from Planet import *
from Sun import *
from LatitudeBelt import *

# Importing Libraries

# Global Variables

number_of_latitude_belts = 10
array_of_latitude_belts = []

# Instantiating Objects

planet = Planet(6.378e6, 23.4, number_of_latitude_belts)
sun = Sun(1.50e11, 3.8e26)

for index in range(number_of_latitude_belts):
  latitude_belt = LatitudeBelt(index, 0)
  array_of_latitude_belts.append(latitude_belt)

# Calculating Power

for index in range(number_of_latitude_belts):
  array_of_latitude_belts[index].power = planet.calculate_power(
    index, sun.luminosity, sun.distance_from_planet)

print(array_of_latitude_belts[0].power)
