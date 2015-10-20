#!/usr/bin/env python
# -*- coding: utf-8 -*-

from planeta import Planeta
import numpy as np


condicion_inicial = [10, 0, 0, 2]

p = Planeta(condicion_inicial)
dt=10

p.avanza_rk4(dt)

