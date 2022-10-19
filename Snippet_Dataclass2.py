# -*- coding: utf-8 -*-
"""
Created on Tue May 17 18:59:52 2022

@author: w.haak
"""

from dataclasses import dataclass, asdict
from math import asin, cos, radians, sin, sqrt

@dataclass
class DataClassCard:
    rank: str
    suit: str

@dataclass
class Position:
    name: str
    lon: float
    lat: float
    
    def distance_to(self, other):
        r = 6371 #Earth radius in km
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2, = radians(self.lat), radians(other.lat)
        h = (sin((phi_2 - phi_1) /2) **2
             + cos(phi_1) * cos(phi_2) * sin ((lam_2 - lam_1) /2)**2)
        return 2 * r * asin(sqrt(h))
        
    
@dataclass
class CrvObs:
    handle : int
    vertlist : dict
    splid: int
    vertpos : dict


def main():
    """Main entry  point of the file"""
    
    def CardStuff():
        QOfHearts = DataClassCard('Q', 'Hearts')
        print(QOfHearts.rank)
    
        print(QOfHearts == DataClassCard('Q', 'Hearts'))
    
    def PosStuff():
        Oslo = Position('Oslo', 10.8, 59.9)
        Vancouver = Position('Vancouver', -123.1, 49.3)
        print(Oslo.lat )
        print(f"{Oslo.name} is at {Oslo.lat}N, {Oslo.lon}E")
        print(Oslo.distance_to(Vancouver))
    
    PosStuff()
    shape = CrvObs(1, {'1':1}, 1, {'1':0})
    print(shape)
    CrvObs.handle = 2
    print(CrvObs.handle)
    
if __name__ == "__main__":
    main() 