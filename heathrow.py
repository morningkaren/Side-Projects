import numpy as np

fname = 'heathrowdata.txt'
dtype1 = np.dtype([('year', 'f8'), ('month', 'f8'), ('maxtemp', 'f8'), ('mintemp', 'f8'), ('rainfall', 'f8'), ('sun', 'S8')])
a = np.loadtxt(fname, dtype=dtype1, skiprows=7, usecols=(0,1,2,3,5,6))


out_arr_max_temp = np.argsort(a['maxtemp'])
#print(out_arr_max_temp)
print("\n")
print(a['year'][out_arr_max_temp][-10:])
#prints out sorted max temperature by year starting from the tenth to last year
print(a['month'][out_arr_max_temp][-10:])
#prints out sorted max temperature by month starting from the tenth to last month.

print(f"The first hottest date is {(a[702][1])}, {a[702][0]}, with a temperature of {a[702][2]} degrees celcius.")
print(f"The second hottest date is {a[426][1]}, {a[426][0]}, with a temperature of {a[426][2]} degrees celcius.")
print(f"The third hottest date is {a[786][1]}, {a[786][0]}, with a temperature of {a[786][2]} degrees celcius.")
print(f"The fourth hottest date is {a[571][1]}, {a[571][0]}, with a temperature of {a[571][2]} degrees celcius.")
print(f"The fifth hottest date is {a[342][1]}, {a[342][0]}, with a temperature of {a[342][2]} degrees celcius.")
print(f"The sixth hottest date is {a[667][1]}, {a[667][0]}, with a temperature of {a[667][2]} degrees celcius.")
print(f"The seventh hottest date is {a[570][1]}, {a[570][0]}, with a temperature of {a[570][2]} degrees celcius.")
print(f"The eighth hottest date is {a[558][1]}, {a[558][0]}, with a temperature of {a[558][2]} degrees celcius.")
print(f"The ninth hottest date is {a[511][1]}, {a[511][0]}, with a temperature of {a[511][2]} degrees celcius.")
print(f"The tenth hottest date is {a[331][1]}, {a[331][0]}, with a temperature of {a[331][2]} degrees celcius.")

mintemp_min = np.argsort(a['mintemp'])
#print(mintemp_min)
print("\n")
print(a['year'][mintemp_min][0:11])
#prints out the sorted minimum temperature by year, the first ten lowest years.
print(a['month'][mintemp_min][0:11])
#prints out the sorted minimum temperature by month, the first ten lowest months..

print(f"The first coldest date is {a[180][1]}, {a[180][0]}, with a temperature of {a[180][3]} degrees celcius.")
print(f"The second coldest date is {a[97][1]}, {a[97][0]}, with a temperature of {a[97][3]} degrees celcius.")
print(f"The third coldest date is {a[457][1]}, {a[457][0]} with a temperature of {a[457][3]} degrees celcius.")
print(f"The fourth coldest date is {a[372][1]}, {a[372][0]} with a temperature of {a[372][3]}degrees celcius.")
print(f"The fifth coldest date is {a[181][1]}, {a[181][0]} with a temperature of {a[181][3]} degrees celcius.")
print(f"The sixth coldest date is {a[444][1]}, {a[444][0]} with a temperature of {a[444][3]} degrees celcius.")
print(f"The seventh coldest date is {a[407][1]}, {a[407][0]} with a temperature of {a[407][3]} degrees celcius.")
print(f"The eighth coldest date is {a[755][1]}, {a[755][0]} with a temperature of {a[755][3]} degrees celcius.")
print(f"The ninth coldest date is {a[517][1]}, {a[517][0]} with a temperature of {a[517][3]} degrees celcius.")
print(f"The tenth coldest date is {a[179][1]}, {a[179][0]} with a temperature of {a[179][3]} degrees celcius.")

list_of_rainfalls = []
n= 1948
while n < 2017:
    m = n == a['year']
    list_of_rainfalls.append((a['rainfall'][m]))
    n += 1
    #print(list_of_rainfalls)

list_of_lists = [individual_arrays.tolist() for individual_arrays in list_of_rainfalls]
print(list_of_lists)
#list comprehension, brackets needed to turn list of arrays into lists of lists)
print("\n")


n = -1
individual_sums = []
while n < 68:
    n += 1
    d = sum(list_of_lists[n])
    individual_sums.append(d)

print(individual_sums)

index_of_max = individual_sums.index(max(individual_sums))

print(index_of_max)

print(66*12)

print(a['year'][792])
#prints out the year with the greatest amount of list_of_rainfalls

k = [i if i!=b'---' else 999 for i in a['sun']]
#list comprehension, replacing all '---' with 999.

j = [float(i) for i in k]
#list comprehension, replacing all elements as floats.
#print(j)

#print(a['month'])

mydictionary = dict(zip(j, a['month']))

#print(mydictionary)

june_month_sun = [sunlight for sunlight, month in mydictionary.items() if month == 6.0]
print(june_month_sun)

print(min(june_month_sun))

index_of_min_sun = j.index(min(june_month_sun))

print(index_of_min_sun)

print(a['year'][821])

print(f"The least sunny june occured in the year {a['year'][821]}.")
