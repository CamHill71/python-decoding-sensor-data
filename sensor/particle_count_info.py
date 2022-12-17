# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 13:38:14 2022

@author: Cameron Hill
"""


from house_info import HouseInfo
from datetime import date


class ParticleData(HouseInfo):

    def _convert_data(self, data):
        recs = []

        for rec in data:
            recs(float(rec))

        return recs

    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area("particulate", rec_area)
        return self._convert_data(recs)

    def get_data_by_date(self, rec_date=date.today()):
        recs = super().get_data_by_date("particulate", rec_date)
        return self._convert_data(recs)
