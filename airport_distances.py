# omicron = d/r where theta is the central angel between two points on a sphere
#and d = distacne between the two points along a great circle of the sphere
#r is the radius of the sphere.
#hav(omicron) = hav(alpha2- alpha1) + cos(alpha1)cos(alpha2)hav(beta2-beta1)
#alpha1, alpha2: latitude of point 1 and latitude of point 2 (in radians)
#beta1, beta2: longitude of point1 and longitude of point 2(in radians).

#hav(theta) = sin^2(theta/2) = (1-cos(theta))/2

#assume r = 6378.1km

import pandas as pd
import numpy as np
import csv
from math import sqrt
from math import sin
from math import cos
from math import asin

#with open('busiest_airports.csv', 'r') as original: data = original.read()
#with open('busiest_airports.csv', 'w') as modified: modified.write("IATA \t Name \t Location \t Latitude \t Longitude \n" + data)

data = pd.read_csv('busiest_airports.csv', delimiter='\t')
#reading the dataframe using pandas

data['Latitude in Radians'] = ((data.iloc[:, 3:4]*3.14)/180)
#locating the latitudes of places and converting them to Radians

data['Longitude in Radians'] = ((data.iloc[:, 4:5]*3.14)/180)
#locating the longitudes of places and converting them to radians

dftolistIATA = data.iloc[:, 0:1].values.tolist()
flattened_list = []
flattened_list = [y for x in dftolistIATA for y in x]
#a list of lists of the IATAs were created from .values.tolist(), so I needed to create
#a flattened list for my dictionary to work
#why does this work?????

dftolistLatRad = data.iloc[:, 5:6].values.tolist()
flattened_list2 = [y for x in dftolistLatRad for y in x]


dftolistLongRad = data.iloc[:, 6:7].values.tolist()
flattened_list3 = [y for x in dftolistLongRad for y in x]

#I felt creating a dictionary would make it easy to get the corresponding latitude/longitude from an IATA.

mydictionary= dict(zip(flattened_list,  flattened_list2))
mydictionary2= dict(zip(flattened_list, flattened_list3))
#creating dictionaries that map IATAs to their respective latitudes and longitudes


def distance(IATA1, IATA2):
    return 2*(6378.1)*asin(sqrt((sin(.5*mydictionary[IATA2]-.5*mydictionary[IATA1]))**2+ cos(mydictionary[IATA1])*cos(mydictionary[IATA2])*((sin(.5*mydictionary2[IATA2]-.5*mydictionary2[IATA1]))**2)))
#  the distance formula from the haversine function found on wikipedia.
print(distance('AMS', 'JFK'))
