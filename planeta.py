# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 18:36:30 2015

@author: splatt
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scipy.integrate as integrate 

class Planeta(object):
    '''
    Complete el docstring.
    '''
    def __init__(self, condicion_inicial, alpha=0):
        '''
        __init__ es un método especial que se usa para inicializar las
        instancias de una clase.

        Ej. de uso:
        >> mercurio = Planeta([x0, y0, vx0, vy0])
        >> print(mercurio.alpha)
        >> 0.
        '''
        self.y_actual = condicion_inicial
        self.t_actual = 0.
        self.alpha = alpha
        self.energia_actual=0

    def ecuacion_de_movimiento(self,t,s):
        '''
        Implementa la ecuación de movimiento, como sistema de ecuaciónes de
        primer orden.
        '''
        G=6.674e-11 
        M=19891e+17
        x, y, vx, vy = self.y_actual
        dvxdt=G*M*x/(((x**2)+(y**2))**(3./2.))
        dvydt=G*M*y/(((x**2)+(y**2))**(3./2.))
        return [vx, vy, dvxdt, dvydt]

    def avanza_euler(self, dt):
        '''
        Toma la condición actual del planeta y avanza su posicion y velocidad
        en un intervalo de tiempo dt usando el método de Euler explícito. El
        método no retorna nada, pero re-setea los valores de self.y_actual.
        '''
        self.ecuacion_de_movimiento
        pass

    def avanza_rk4(self, dt):
        '''
        Similar a avanza_euler, pero usando Runge-Kutta 4.
        '''
        Ecuacion=self.ecuacion_de_movimiento
        T=[self.t_actual,dt+self.t_actual]
        Ecuacion_integrada=integrate.odeint(Ecuacion, self.y_actual, T)
        self.y_actual=Ecuacion_integrada[1]
        self.t_actual=T[1]
        pass

    def avanza_verlet(self, dt):
        '''
        Similar a avanza_euler, pero usando Verlet.
        '''
        pass

    def energia_total(self):
        '''
        Calcula la enérgía total del sistema en las condiciones actuales.
        '''
        G=6.674e-11 
        M=19891e+17
        m=1/(G*M)
        self.energia_actual=-G*M*m/(((self.y_actual(0)**2)+(self.y_actual(1)**2))**(1./2.))
        pass