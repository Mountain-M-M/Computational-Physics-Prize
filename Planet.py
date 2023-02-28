# import numpy as np
from numpy import *


class Planet:

  def __init__(self, radius, obliquity, num_of_latitude_belts):
    self.radius = radius
    self.obliquity = obliquity
    self.num_of_latitude_belts = num_of_latitude_belts

  def calculate_power(self, index_of_latitude_belt, luminosity,
                      distance_from_sun, albedo, area):
    r = self.radius
    L = luminosity
    D = distance_from_sun
    n = index_of_latitude_belt
    N = self.num_of_latitude_belts
    theta = n / N
    a = albedo
    A = area

    power = L * A * (1 - a) / (4 * pi * D**2)

    return power

  def calculate_energy_emitted(self, stefan, emissivity, area, temperature):
    s = stefan
    e = emissivity
    A = area
    T = temperature
    
    emitted_energy = s * e * A * T ** 4

    return emitted_energy
