# import numpy as np
from numpy import *

class Planet:
  def __init__(self, radius, obliquity, num_of_latitude_belts):
    self.radius = radius
    self.obliquity = obliquity
    self.num_of_latitude_belts = num_of_latitude_belts


  def calculate_power_each_latitude_belt(self, luminosity, distance_from_sun):
    power_of_each_latitude_belt = []
    r = self.radius
    L = luminosity
    D = distance_from_sun

    for n in range(self.num_of_latitude_belts):
      theta = n/self.num_of_latitude_belts
      area_of_latitude_belt = (cos(pi * theta) - cos(pi * (theta + 1/self.num_of_latitude_belts))) * 2 * pi * r

      A = area_of_latitude_belt
      
      power_of_each_latitude_belt.append((L * A) / (4 * pi * D ** 2))
    return power_of_each_latitude_belt
      

  