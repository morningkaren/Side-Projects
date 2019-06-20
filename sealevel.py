import numpy as np
import matplotlib.pyplot as plt
import sys

np.set_printoptions(threshold=sys.maxsize)

#naming .npy file as fname and reading it with numpy
fname = 'gb-alt.npy'
a = np.load(fname)

#when sea levels rise 10m, we reduce the altitude of the land mass by 10. W
#We replace all negative values of the altitudes with 0.
z = a-10
z[z<0] = 0

#sea levels rise 50m, reduce altitude by 50. Replace all negative values of altitudes with 0.
b = a-50
b[b<0] = 0

#sea levels rise 100m, reduce altitude by 100.
c = a-100
c[c<0] = 0

#shows the four different maps, one with original sea level,
#second with sea level rising 10m, third with sea level rising 50m, and fourth with sea level rising 100m
plt.imshow(a, interpolation='nearest', cmap='gray')
plt.show()
plt.imshow(z, interpolation='nearest', cmap='gray')
plt.show()
plt.imshow(b, interpolation='nearest', cmap='gray')
plt.show()
plt.imshow(c, interpolation='nearest', cmap='gray')
plt.show()

#deducing percentage of land area remaining

#number of arrays in A
A= len(a)
#number of elements in each array of A
len(a[0])
#total number of hectad squares
hectad_squares=A* len(a[0])
print(hectad_squares)

#total area of map in km^2
total_area_of_map = hectad_squares * 100
print(total_area_of_map)

counter = 0
for element in a:
    for element in element:
        if element == 0:
            counter += 1
print(counter)

#total non-zero altitude hectad squares
hectad_land_mass = hectad_squares - counter
print(hectad_land_mass)

#total area of land mass in km^2
print(hectad_land_mass * 100)

#land area with sea level rising 10m
counter2 = 0
for element in z:
    for element in element:
        if element == 0:
            counter2 += 1
print(counter2)

hectad_land_mass_10 = hectad_squares - counter2
print(hectad_land_mass_10)
print(hectad_land_mass_10*100)

#percentage of land mass remaining with sea level rising 10m
print((hectad_land_mass_10/hectad_land_mass)*100)

#land area with sea level rising 50m
counter3 = 0
for element in b:
    for element in element:
        if element == 0:
            counter3 += 1
print(counter3)

hectad_land_mass_50 = hectad_squares - counter3
print(hectad_land_mass_50)
print(hectad_land_mass_50 *100)

#percentage of land mass remaining with sea level rising 50m
print((hectad_land_mass_50/hectad_land_mass)*100)

#land area with sea level rising 100m
counter4 = 0
for element in c:
    for element in element:
        if element == 0:
            counter4 += 1
print(counter4)

hectad_land_mass_100 = hectad_squares - counter4
print(hectad_land_mass_100)
print(hectad_land_mass_100 * 100)

#percentage of land mass remaining with sea level rising 100m
print((hectad_land_mass_100/hectad_land_mass)*100)
