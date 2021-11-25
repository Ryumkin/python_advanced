import numpy as np
import pandas as pd

xz = pd.read_csv('1.csv', delimiter=',')

print(xz.columns)
print(max(xz.count()))
print(xz["Sex"].value_counts())
print(f"parch = {xz[xz['Parch'] > 0]['Parch'].count()}")
print(xz["Pclass"].value_counts(normalize=True))

print(f'proportion of survivors among first-class passengers = {round(xz[(xz["Survived"]==1) & (xz["Pclass"]==1)].shape[0]/xz[xz["Pclass"]==1].shape[0],2)}')

print(f'average age = {round(xz["Age"].mean(), 3)}')
print(f'median age = {round(xz["Age"].median(), 3)}')
print(xz["Age"].value_counts())

print(xz[xz["Fare"] > xz["Fare"].mean()].shape[0])
