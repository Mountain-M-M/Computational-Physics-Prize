# Importing Files

from Planet import *
from Sun import *

# Importing Libraries


# Global Variables

planet = Planet(6.378e6, 23.4, 10)
sun = Sun(1.50e11, 3.8e26)




power_array = planet.calculate_power_each_latitude_belt(
  sun.luminosity, sun.distance_from_planet)

print(power_array)
