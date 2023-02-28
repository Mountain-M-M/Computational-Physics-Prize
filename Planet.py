# import numpy as np
from numpy import *


class Planet:

  def __init__(self, radius, obliquity, num_of_latitude_belts):
    self.radius = radius
    self.obliquity = obliquity
    self.num_of_latitude_belts = num_of_latitude_belts

  def calculate_power(self, index_of_latitude_belt, luminosity,
                      distance_from_sun):
    r = self.radius
    L = luminosity
    D = distance_from_sun
    n = index_of_latitude_belt
    N = self.num_of_latitude_belts
    theta = n / N

    area = (cos(pi * theta) - cos(pi * (theta + 1 / N))) * 2 * pi * r

    A = area

    power = (L * A) / (4 * pi * D**2)

    return power
