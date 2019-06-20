import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
import matplotlib.patches as mpatches

population = 'population_total.tsv'
bmi = 'bmi_men.tsv'
gdp = 'gdp.tsv'
colordata = 'continents.tsv'

pop_data = pd.read_csv(population, sep = '\t', header=None)
bmi_data = pd.read_csv(bmi, sep = '\t', header=None)
gdp_data = pd.read_csv(gdp, sep = '\t', header=None)
color_data = pd.read_csv(colordata, sep = '\t', header=None)


def dictionarymaking(list_of_lists1, list_of_lists2):
    the_list1 = []
    the_list2 = []
    flattened_list1 = []
    flattened_list2 = []
    the_tuple_list = []
    for element in list_of_lists1:
        the_list1.append(element)
        flattened_list1 = [y for x in the_list1 for y in x]
    for element in list_of_lists2:
        the_list2.append(element)
        flattened_list2 = [y for x in the_list2 for y in x]
        mydictionary = dict(zip(flattened_list1, flattened_list2))
    return mydictionary

bmi_dictionary = dictionarymaking(bmi_data.iloc[:, 0:1].values.tolist(), bmi_data.iloc[:, 1:2].values.tolist() )

#print(bmi_dictionary)

gdp_dictionary = dictionarymaking(gdp_data.iloc[:,0:1].values.tolist(), gdp_data.iloc[:,1:2].values.tolist())

#print(gdp_dictionary)

pop_dictionary = dictionarymaking(pop_data.iloc[:,0:1].values.tolist(), pop_data.iloc[:,1:2].values.tolist())

#print(pop_dictionary)
color_dictionary= dictionarymaking(color_data.iloc[:,0:1].values.tolist(), color_data.iloc[:,1:2].values.tolist())


for country, continent in color_dictionary.items():
    if continent == 'Europe':
        color_dictionary[country] = 'red'

for country, continent in color_dictionary.items():
    if continent == 'Asia':
        color_dictionary[country] = 'orange'

for country, continent in color_dictionary.items():
    if continent == 'Oceania':
        color_dictionary[country] = 'yellow'

for country, continent in color_dictionary.items():
    if continent == 'Africa':
        color_dictionary[country] = 'green'

for country, continent in color_dictionary.items():
    if continent == 'North America':
        color_dictionary[country]= 'blue'

for country, continent in color_dictionary.items():
    if continent == 'South America':
        color_dictionary[country] = 'purple'

for color, continent in color_dictionary.items():
    if continent == 'None':
        color_dictionary[country] = 'black'

print(color_dictionary)


list_of_bmi_gdp = []
for element in gdp_dictionary.keys():
    if element in bmi_dictionary.keys():
        list_of_bmi_gdp.append((bmi_dictionary[element], gdp_dictionary[element], pop_dictionary[element]/8000000, color_dictionary.get(element, 'None')))

red_patch = mpatches.Patch(color='red', label='Europe')
orange_patch=mpatches.Patch(color='orange', label='Asia')
yellow_patch=mpatches.Patch(color='yellow', label='Oceania')
green_patch=mpatches.Patch(color='green', label='Africa')
blue_patch=mpatches.Patch(color='blue',label='North America')
purple_patch=mpatches.Patch(color='purple', label='South America')

x,y,z, q= zip(*list_of_bmi_gdp)
plt.scatter(x,y,s=z, c=q)
plt.xlabel('BMI of men')
plt.ylabel('GDP per person per capita in 2005')
plt.legend(handles=[red_patch, orange_patch, yellow_patch, green_patch, blue_patch, purple_patch])
plt.title('Body Mass Index vs Gross Domestic Product')
plt.show()
