# import numpy as np
from numpy import *


class LatitudeBelt:
  
  def __init__(self, index, albedo, temperature, emissivity, area):
    self.index = index
    # self.power = power
    self.albedo = albedo
    self.area = area
    self.temperature = temperature
    self.emissivity = emissivity
    # self.energy_emitted = energy_emitted

  def calculate_area(self, index, number_of_latitude_belts, radius):
    N = number_of_latitude_belts
    n = index
    theta = n / N
    r = radius
    
    area = (cos(pi * theta) - cos(pi * (theta + 1 / N))) * 2 * pi * r
    
    return area

  def calculate_power(self, radius, luminosity, distance_from_sun, num_of_latitude_belts):
    r = radius
    L = luminosity
    D = distance_from_sun
    n = self.index
    N = num_of_latitude_belts
    theta = n / N
    a = self.albedo
    A = self.area

    power = (1 - a) * (L * r * (arccos(theta * n / r) - arccos(theta * (n+1) / r))) / (A * D)

    return power
    

  def calculate_energy_emitted(self, stefan):
    s = stefan
    e = self.emissivity
    A = self.area
    T = self.temperature
    
    energy_emitted = s * e * A * T ** 4
    return energy_emitted
