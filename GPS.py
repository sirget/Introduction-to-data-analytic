# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 14:51:28 2021

@author: Pnach
"""

import numpy as np
import pandas as pd
import folium
from folium import plugins

df = pd.read_csv(
    "/2018-12-25/2018-12-25.00.csv")
print(df.to_string())
