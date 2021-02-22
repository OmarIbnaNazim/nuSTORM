#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for "nuSTORMPrdStrght" class
========================================

  Assumes python path includes nuSim code.

  Script starts by testing built in methods.  Then a soak test with a set 
  of reference plots.

"""

import nuSTORMPrdStrght as nuStrt
import numpy as np
import matplotlib.pyplot as plt
from Simulation import *

##! Start:
print("========  nuSTORMPrdStrght: tests start  ========")

##! Test singleton class feature:
nuSTORMPrdStrghtTest = 1
print()
print("nuSTORMPrdStrghtTest:", nuSTORMPrdStrghtTest, " check if class is a singleton.")
nuPrdStrt  = nuStrt.nuSTORMPrdStrght('11-Parameters/nuSTORM-PrdStrght-Params-v1.0.csv')
nuPrdStrt1 = nuStrt.nuSTORMPrdStrght('11-Parameters/nuSTORM-PrdStrght-Params-v1.0.csv')
print("    nuPrdStrt singleton test:", id(nuPrdStrt), id(nuPrdStrt1), id(nuPrdStrt)-id(nuPrdStrt1))
if nuPrdStrt != nuPrdStrt1:
    raise Exception("nuSTORMPrdStrght is not a singleton class!")

##! Check built-in methods:
nuSTORMPrdStrghtTest = 2
print()
print("nuSTORMPrdStrghtTest:", nuSTORMPrdStrghtTest, " check built-in methods.")
print("    __repr__:")
print(nuPrdStrt)

##! Check get methods:
nuSTORMPrdStrghtTest = 3
print()
print("nuSTORMPrdStrghtTest:", nuSTORMPrdStrghtTest, " check get methods.")
print("----> printParams() method; reports parameters loaded")
nuPrdStrt.printParams()

##! Check momentum, z, and transverse distributions:
nuSTORMPrdStrghtTest = 4
print()
print("nuSTORMPrdStrghtTest:", nuSTORMPrdStrghtTest, " momentum distribution.")
pmu = np.array([])
nmu = 0
zmu = np.array([])
xmu = np.array([])
ymu = np.array([])
xpmu = np.array([])
ypmu = np.array([])
print()
for i in range(100000):
  nmu += 1
  pmu = np.append(pmu, nuPrdStrt.GenerateMmtm(5.))
  zmu = np.append(zmu, nuPrdStrt.Calculatez(50.*getRandom()))
  x, y, xp, yp = nuPrdStrt.GenerateTrans(50.*getRandom())
  xmu  = np.append(xmu, x)
  ymu  = np.append(ymu, y)
  xpmu = np.append(xpmu, xp)
  ypmu = np.append(ypmu, yp)
  if nmu < 11:
      print(nmu, pmu[nmu-1], zmu[nmu-1], x, y, xp, yp)

n, bins, patches = plt.hist(pmu, bins=50, color='y', range=(4.5,5.5))
plt.xlabel('Momentum (GeV)')
plt.ylabel('Entries')
plt.title('momentum distribution')
plt.show()
n, bins, patches = plt.hist(zmu, bins=50, color='y', range=(0.,50.))
plt.xlabel('z (m)')
plt.ylabel('Entries')
plt.title('z distribution')
plt.show()
n, bins, patches = plt.hist(xmu, bins=50, color='y', range=(-0.15,0.15))
plt.xlabel('x (m)')
plt.ylabel('Entries')
plt.title('x distribution')
plt.show()
n, bins, patches = plt.hist(ymu, bins=50, color='y', range=(-0.15,0.15))
plt.xlabel('y (m)')
plt.ylabel('Entries')
plt.title('y distribution')
plt.show()
n, bins, patches = plt.hist(xpmu, bins=50, color='y', range=(-0.0075,0.0075))
plt.xlabel('x^prime')
plt.ylabel('Entries')
plt.title('x^prime distribution')
plt.show()
n, bins, patches = plt.hist(ypmu, bins=50, color='y', range=(-0.0075,0.0075))
plt.xlabel('y^prime')
plt.ylabel('Entries')
plt.title('y^prime distribution')
plt.show()
  

##! Complete:
print()
print("========  nuSTORMPrdStrght: tests complete  ========")
