import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fontTools.subset import subset # pycharm put this in for me??
from icecream import ic
import cartopy as cp

import fun_eda_demo as fd
import fun_grid as fg

data = pd.read_csv('/Users/shartface/Documents/GitHub/ev228_individual-analysis/Data/NAS-Specimen-Download.csv')
ic(data)

# sample some stuff
years = (data['Year'].iloc[0], data['Year'].iloc[(len(data) // 2)],data['Year'].iloc[-1])
lats = (data['Latitude'].iloc[0], data['Latitude'].iloc[(len(data) // 2)],data['Latitude'].iloc[-1])
lons = (data['Longitude'].iloc[0], data['Longitude'].iloc[(len(data) // 2)],data['Longitude'].iloc[-1])
ic(years, lats, lons)

#  Check dimensions
dims = np.shape(data)
ic(dims)

# drop empty cells just for the column we want to work with (prevents excess removal- i think?)
clean_month = data.dropna(subset='Month')
clean_lat = data.dropna(subset='Latitude')
clean_lon = data.dropna(subset='Longitude')
clean_recordtype = data['Type 1'].fillna('Personal Communication')

# data analysus
yr_anal = fd.descriptive_statistics(data['Year'])
month_anal = fd.descriptive_statistics(clean_month['Month'])
lat_anal = fd.descriptive_statistics(clean_lat['Latitude'])
lon_anal = fd.descriptive_statistics(clean_lon['Longitude'])
ic(yr_anal,month_anal,data['Month'].describe(),lat_anal,lon_anal) # i learned that .describe does exactly what our descriptive stats do #wow


# year work
all_year_list = data['Year'].sort_values() #create list of years sequentially
year_list = set(all_year_list) #remove duplicate years - this does nothing for me in the end, but set() is cool
# ic(year_list)
# create a year count representing how many times each year is present
year_count = {}
for i in all_year_list:
    if i not in year_count:
        year_count[i] = 1
    else:
        year_count[i] += 1

# Create year figure
fig1, ax1 = plt.subplots()
plt.bar(year_count.keys(), year_count.values())
ax1.spines[['right', 'top']].set_visible(False)
plt.xlabel('Year')
plt.ylabel('Number of Reported Sightings')
plt.title('Number of Zebra Mussel Reported Sightings per Year')
plt.savefig('/specimen-yearcount.png')


# month work
all_month_list =clean_month['Month'].sort_values() #create list of months sequentially
ic(all_month_list)
# create dict: keys = months, values = month count
month_count = {}
for i in all_month_list:
    if i not in month_count:
        month_count[i] = 1
    else:
        month_count[i] += 1
ic(month_count)

# Create month figure
fig2, ax2 = plt.subplots()
plt.bar(month_count.keys(), month_count.values())
ax2.spines[['right', 'top']].set_visible(False)
plt.xlabel('Month')
plt.ylabel('Number of Reported Sightings')
plt.title('Number of Zebra Mussel Reported Sightings per Month Across All Years')
plt.xticks(range(1,13),['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
     'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.savefig('/specimen-monthcount.png')


# record type work
record_count = {}
for i in clean_recordtype:
    if i not in record_count:
        record_count[i] = 1
    else:
        record_count[i] += 1
#change name of other column
record_count['Other Literature'] = record_count.pop('Other')
ic(record_count)

# create record type figure
fig4, ax4 = plt.subplots()
ax4.spines[['right', 'top']].set_visible(False)
plt.barh(record_count.keys(),record_count.values())
plt.xlabel('Number of Reported Sightings')
plt.ylabel('Record Type')
plt.title('Number of Zebra Mussel Reported Sightings per Record Type')
fig4.tight_layout()
plt.savefig('/specimen-recordtype.png', bbox_inches='tight')


# map
fig3, ax3 = plt.subplots(
    1, 1,
    subplot_kw={"projection": cp.crs.LambertConformal(
        central_longitude=-100,
        central_latitude=45)})
d_crs = cp.crs.PlateCarree()

# set map boundaries
ax3.set_extent([-120, -72, 25, 55], crs=d_crs)
lat = data['Latitude']
lon = data['Longitude']
image = ax3.scatter(lon,lat,transform=d_crs,c=data['Year'],cmap='turbo',s=10)
ax3.coastlines()

# # add color map
colorbar = plt.colorbar(image)
colorbar.set_label('Reported Year')

plt.title('Zebra Mussel Reported Sightings')
plt.savefig('/colormap.png')

