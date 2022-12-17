# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 13:38:14 2022

@author: Cameron Hill
"""

from house_info import HouseInfo

class EnergyData(HouseInfo):

    ENERGY_PER_BULB = 0.2
    ENERGY_BITS = 0x0f0

    def _get_energy(self, rec):
        energy = int(rec,base=16)
        energy = energy & self.ENERGY_BITS
        energy = energy >> 4

        return energy








