#!/usr/bin/env python
# -*- coding: utf-8 -*-

from planeta import Planeta
import numpy as np
import matplotlib.pyplot as plt


condicion_inicial = [10, 0, 0, 2]

p = Planeta(condicion_inicial)
dt=np.linspace(0,100,101)
Energias=[]
X=[]
Y=[]
for i in (dt):
    p.avanza_rk4(dt[i])
    Energias.append(p.energia_actual)
    X.append(p.y_actual[0])
    Y.append(p.y_actual[1])
plt.figure(1)
plt.plot(Energias, dt)
plt.xlabel('energia',fontsize=18)
plt.ylabel('tiempo', fontsize=18)
plt.figure(2)
plt.plot(X, Y)
plt.xlabel('x', fontsize=18)
plt.ylabel('y', fontsize=18)
