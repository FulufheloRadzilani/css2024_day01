# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:44:25 2024

@author: radzi
"""

import pandas as FR
file = FR.read_csv("country_data.csv")
print(file)
"""
    Age Gender       Country
0    39      M  South Africa
1    25      M      Botswana
2    29      F  South Africa
3    46      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    49      M         Kenya
8    30      M         Kenya
9    40      F         Egypt
10   30      M         Sudan
"""
age1 = 30
age2 = 25
age3 = 29

age = [30,25,29,46,22]

print(age)


print(age[0])


print(age[1])
print(min(age))

print(max(age))

print(sum(age))

print(len(age))

avg = sum(age)/len(age)

print(avg)

g1 = "M"
g2 = "F"
g3 = "M"

gender = ["M", "F", "F"]

C1 = "South Africa"
c2 = "Lesotho"

print(age[0:3])

age.append(100)
print(100)

age.insert(4,100)
print(age)
"""

Dictionaries - key:value pairs

cat: "a cute animal"
"""

mammals = {"cat":"a cute animal", "lion": "king of the jungles", "elephant": "a gigantic herbivore"}

print(mammals["cat"])

"""
Data frames
"""

fruits = ["peache", "leaches", "pamogrenade", "mangoes", "pineapple"]

size_nm = [9.8, 10.1, 13.2, 8.7, 20.5]

fruit_size = {
    "fruits": fruits,
    "size": size_nm
    
    }

"""
df = dataframe
"""

import pandas as FR
df = FR.DataFrame(fruit_size)

print(df["fruits"])
print(df["size"])
print(df["size"].min())
print(df["size"].mean())
print(df.describe())
print(df[df["size"]> 10])
print(df[1:3])

prices = [10.00, 12.50, 16.00, 23.00, 7.00]

df["prices"] = prices

df.drop(columns=["size"], inplace=True)


