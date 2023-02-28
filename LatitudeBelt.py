# import numpy as np
from numpy import *


class LatitudeBelt:
  
  def __init__(self, index, power, albedo, area, temperature, emissivity, energy_emitted):
    self.index = index
    self.power = power
    self.albedo = albedo
    self.area = area
    self.temperature = temperature
    self.emissivity = emissivity
    self.energy_emitted = energy_emitted

  def calculate_area(self, index, number_of_latitude_belts, radius):
    N = number_of_latitude_belts
    n = index
    theta = n / N
    r = radius
    
    area = (cos(pi * theta) - cos(pi * (theta + 1 / N))) * 2 * pi * r
    
    return area

  def calculate_power():
    pass

  def calculate_energy_emitted():
    pass