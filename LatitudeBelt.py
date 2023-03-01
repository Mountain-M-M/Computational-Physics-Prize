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
    theta = pi / N
    r = radius
    
    area = (cos(n * theta) - cos(theta * (1 + n))) * 2 * pi * r ** 2
    
    return area

  def calculate_power(self, radius, luminosity, distance_from_sun, num_of_latitude_belts):
    L = luminosity
    D = distance_from_sun
    a = self.albedo
    A = self.area

    intensity = L / (4 * pi * D ** 2)

    I = intensity

    power = I * A * (1 - a)

    return power
    

  def calculate_energy_emitted(self, stefan):
    s = stefan
    e = self.emissivity
    A = self.area
    T = self.temperature
    
    energy_emitted = s * e * A * T ** 4
    return energy_emitted
