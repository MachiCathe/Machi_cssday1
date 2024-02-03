# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 23:21:40 2024

@author: 20090187
"""

import pandas

file = pandas.read_csv("country_data.csv")

print(file)

print(file.info())

print(file.describe())


file = pandas.read_csv("iris.csv")

print(file)

print(file.info())

print(file.describe())


file = pandas.read_csv("insurance_data.csv", skiprows=5)

print(file)

print(file.info())

print(file.describe())


file = pandas.read_csv("diab_data.csv")

print(file)

file = pandas.read_csv("housing_data.csv")

print(file)



# column_names = ['A','B','C',]

# file = pandas.read_csv("housind_data.csv",names = column_names)


file = pandas.read_csv("housing_data.csv")

print(file)


column_names = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N']

file = pandas.read_csv("housing_data.csv",names = column_names)











