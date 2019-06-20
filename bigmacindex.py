import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

argentina = 'argentina-bigmac.txt'
australia = 'australia-bigmac.txt'
china = 'china-bigmac.txt'
uk = 'uk-bigmac.txt'
usa = 'us-bigmac.txt'

dtype1 = np.dtype([('month', None), ('year', None), ('big mac in currency', None), ('currency/usd', None)])
dtype2 = np.dtype([('month', None), ('year', None), ('big mac in currency', None)])

ar = np.loadtxt(argentina, dtype= dtype1, skiprows=(1), usecols=(0,1,2,3))
au = np.loadtxt(australia, dtype= dtype1, skiprows=(1), usecols=(0,1,2,3))
ch = np.loadtxt(china, dtype = dtype1, skiprows =(1), usecols = (0,1,2,3))
u = np.loadtxt(uk, dtype=dtype1, skiprows=(1), usecols=(0,1,2,3))
us = np.loadtxt(usa, dtype= dtype2, skiprows=(1), usecols = (0,1,2))

ar_price_converted_USD = ar['big mac in currency']*(1/ar['currency/usd'])

au_price_converted_USD = au['big mac in currency']*(1/au['currency/usd'])

ch_price_converted_USD = ch['big mac in currency']*(1/ch['currency/usd'])

uk_price_converted_USD = u['big mac in currency']*(1/u['currency/usd'])

percentage_of_valuation_ar = ((ar_price_converted_USD - us['big mac in currency'])/us['big mac in currency'])*100

percentage_of_valuation_au = ((au_price_converted_USD- us['big mac in currency'])/us['big mac in currency'])*100

percentage_of_valuation_ch = ((ch_price_converted_USD - us['big mac in currency'])/us['big mac in currency'])*100

percentage_of_valuation_uk = ((uk_price_converted_USD - us['big mac in currency'])/us['big mac in currency'])*100

month_ar = ar['month']
year_ar = ar['year']
list_of_months_ar= month_ar.tolist()
list_of_years_ar= year_ar.tolist()

list_of_months_ar_int = []
for month in list_of_months_ar:
    list_of_months_ar_int.append(int(month))

#print(list_of_months_ar_int)

list_of_years_ar_int = []
for year in list_of_years_ar:
    list_of_years_ar_int.append(int(year))

n = -1
list_of_month_years= []
while n < 28:
    n +=1
    list_of_month_years.append((list_of_years_ar_int[n], list_of_months_ar_int[n]))
#print (list_of_month_years)

dt = []
for element in list_of_month_years:
    dt_obj = datetime(*element, 1)
    dt.append(dt_obj)
print(dt)

plt.plot(dt, percentage_of_valuation_ar)
plt.title('Argentina- Change in Percentage of valuation of ARS')
plt.xlabel('Time')
plt.ylabel('Valuation compared to USD')
plt.show()


plt.plot(dt, percentage_of_valuation_au)
plt.title('Australia- Change in Percentange of valuation of AUD')
plt.xlabel('Time')
plt.ylabel('Valuation compared to USD')
plt.show()

plt.plot(dt, percentage_of_valuation_ch)
plt.title('China-Change in Percentage of valuation of CNY')
plt.xlabel('Time')
plt.ylabel('Valuation compared to USD')
plt.show()

plt.plot(dt, percentage_of_valuation_uk)
plt.title('UK-Change in Percentage of valuation of GBP')
plt.xlabel('Time')
plt.ylabel('Valuation compared to USD')
plt.show()
