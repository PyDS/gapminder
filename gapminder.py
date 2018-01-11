'''
Cleaning of Gapminder Data
Data is about Life Expectancy of People of 19th,20th and 21st Century of Different Countries
It is in the format of CSV(Comma Seperated Values)
'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re

#Importing DataSet as gapminder
gapminder = pd.read_csv("gapminder.csv")

#print(g1800s.info())


'''
#===============================================================
#Checking for the valid and null values
def check_null_or_valid(row_data):
	"""Function that takes a row of data,
	drops all missing values,
	and checks if all remaining values are greater than or equal to 0
	"""
	no_na = row_data.dropna()[1:-1]
	numeric = pd.to_numeric(no_na)
	ge0 = numeric >= 0
	return ge0

# Checking whether the first column is 'Life expectancy'
assert gapminder.columns[0] == 'Life expectancy'

# Checking whether the values in the row are valid
assert gapminder.iloc[:, 1:].apply(check_null_or_valid, axis=1).all().all()

# Checking that there is only one instance of each country
assert gapminder['Life expectancy'].value_counts()[0] ==1
#=============================================================
'''

#Reshaping Data by Melting
'''
=========================================================
# Melting gapminder
gapminder_melt = pd.melt(frame=gapminder, id_vars='Life expectancy')

# Renaming the columns
gapminder_melt.columns = ['country','year','life_expectancy']

# Printing the head of gapminder_melt
print(gapminder_melt.head())
==========================================================
'''


#Checking and Converting Data Types
'''
==========================================================
#year column to numeric
gapminder.year = pd.to_numeric(gapminder.year)

#Testing if country is of type object
assert gapminder.country.dtypes == np.object

#year is of type int64
assert gapminder.year.dtypes == np.int64

#life_expectancy is of type float64
assert gapminder.life_expectancy.dtypes == np.float64
===========================================================
'''


#Trying to seperate out the invalid names of countries
'''
=========================================================
# Creating the series of countries
countries = gapminder['country']

# Droping all duplicates from countries
countries = countries.drop_duplicates()

# Writing regex
pattern = '^[A-Za-z\.\s]*$'

# Creating Boolean vector
mask = countries.str.contains(pattern)

# Inverting the mask
mask_inverse = ~mask

# Subseting countries
invalid_countries = countries.loc[mask_inverse]

# Printing invalid_countries
print(invalid_countries)
===========================================================
'''

#Dropping NaN values
'''
==========================================================
# Asserting that country does not contain any missing values
assert pd.notnull(gapminder.country).all()

# Asserting that yaer does not contain any missing values
assert pd.notnull(gapminder.year).all()

# Dropping the missinf values
gapminder = gapminder.dropna()

# Printing the gapminder's shape
print(gapminder.shape)
==========================================================
'''
'''
Creating Plot

#first subplot
plt.subplot(2, 1, 1) 

#histogram of life_expectancy
gapminder.life_expectancy.plot(kind='hist')

# Grouping gapminder
gapminder_agg = gapminder.groupby('year')['life_expectancy'].mean()

#head of gapminder_agg
print(gapminder_agg.head())

#tail of gapminder_agg
print(gapminder_agg.tail())

#second subplot
plt.subplot(2, 1, 2)

#line plot of life expectancy per year
gapminder_agg.plot()

plt.title('Life expectancy over the years')
plt.ylabel('Life expectancy')
plt.xlabel('Year')
plt.tight_layout()
plt.show()

# Exporting DataFrames to csv files
gapminder.to_csv('gapminder.csv')
gapminder_agg.to_csv('gapminder_agg.csv')