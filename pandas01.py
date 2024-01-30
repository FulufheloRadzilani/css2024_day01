# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:39:04 2024

@author: radzi
"""

import pandas as pd
file = pd.read_csv('country_data.csv')

print(file)

print(file.info())

print(file.describe())
file_2 = pd.read_csv('diab_data.csv')
print(file_2)

print(file.describe())
file_3 = pd.read_csv('diab_data.csv')
print(file_3)
print(file_2.info())
print(file_2.describe())

file_3 = pd.read_csv('housing_data.csv')

print(file_3)
print(file_3.info())
print(file_3.describe())

file_4 = pd.read_csv('iris.csv')

print(file_4)
print(file_4.info())
print(file_4.describe())

file_5 = pd.read_csv('insurance_data.csv')

print(file_5)




















