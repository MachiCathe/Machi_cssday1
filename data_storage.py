# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 10:33:28 2024

@author: 20090187
"""

"""
Storing Data in Python
"""

import pandas

file = pandas.read_csv("country_data.csv")

print(file)

# Inputting data from scratch, we have to create variables

age1 = 30
age2 = 25
age3 = 29

# this is tedious especially if you have a  1000 variables, you create lists

age = [30,25,29,46,22]

print(age)

print(age[0])

print(age[1])


print(max(age))

print(len(age))

print(sum(age))

avg = sum(age)/len(age)

print(avg)

# examples of variable list for gender

g1 = "M"
g2 = "F"
g3 = "M"

gender = ["M","F","M"]

    
age.append(100)
print(age)

age.insert(0,100)
print(age)

"""
#dictionaries - key:value pairs

key:value

e.g. cat: cute animal

"""

# Creating a dictionary

mammals = {"cat":"a cute animal","lion":"king of the jungle","elephant":"a gigantic herbivore"}


print(mammals["cat"])

"""
Data frames
"""

fruits = ["apple", "banana", "orange", "grape", "kiwi"]

Size_nm = [9.8, 10.1, 13.2, 8.7, 20.5]

fruit_sizes = {
    
    'fruits' : fruits,
    'sizes' :Size_nm
    }



df = pandas.DataFrame(fruit_sizes)

print(df['fruits'])

print(df['sizes'].mean())

print(df.describe())

print(df[df['sizes']> 10])

print(df[1:3])

prices = [10.00, 12.50, 16.00, 23.00, 7.00]
df['prices'] = prices

df.drop(columns=["sizes"], inplace=True)




























