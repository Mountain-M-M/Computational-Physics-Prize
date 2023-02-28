# import numpy as np
from numpy import *


class LatitudeBelt:

  area = (cos(pi * theta) - cos(pi * (theta + 1 / N))) * 2 * pi * r
  
  def __init__(self, index, power, albedo, temperature, emissivity):
    self.index = index
    self.power = power
    self.albedo = albedo
    self.temperature = temperature
    self.emissivity
    