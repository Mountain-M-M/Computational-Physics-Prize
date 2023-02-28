# Importing Files

from Planet import *
from Sun import *
from LatitudeBelt import *

# Global Variables

number_of_latitude_belts = 10
array_of_latitude_belts = []
albedo = 0.3
stefan = 5.670e-8

# Instantiating Objects

planet = Planet(6.378e6, 23.4, number_of_latitude_belts)
sun = Sun(1.50e11, 3.8e26)

for index in range(number_of_latitude_belts):
  latitude_belt = LatitudeBelt(index, 0, albedo, 0, 0, 0, 0)
  latitude_belt.area = latitude_belt.calculate_area(index, number_of_latitude_belts, planet.radius)

  array_of_latitude_belts.append(latitude_belt)

# Calculating Energy Input

index = 0
for latitude_belt in array_of_latitude_belts:
  latitude_belt.power = planet.calculate_power(index, sun.luminosity, sun.distance_from_planet, latitude_belt.albedo, latitude_belt.area)
  index += 1

print(array_of_latitude_belts[0].power)

# Calculating Emitted Energy

for latitude_belt in array_of_latitude_belts:
  latitude_belt.energy_emitted = planet.calculate_energy_emitted(stefan, latitude_belt.emissivity, latitude_belt.area)
