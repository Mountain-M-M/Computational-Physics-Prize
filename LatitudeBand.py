# import numpy as np
from numpy import *


class LatitudeBand:

  def __init__(self, power, albedo, emissivity, index):
    self.power = power
    self.albedo = albedo
    self.emissivity = emissivity
    self.index = index
