import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('bicycle_data.csv')

print(df.head())
print(df.dtypes)
print(df.columns)

# Date: Date and time of the observation Date                           expected type: datetime
# Fremont Bridge Sidewalks, south of N 34th St Total                    float 64
# Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk    float 64
# Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk    float 64

df['Date'] = pd.to_datetime(df["Date"], format = "%m/%d/%Y %I:%M:%S %p")
west = "Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk"
east = "Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk"
df['sum'] = df[west] + df[east]
df['Hour'] = df['Date'].dt.hour
df['Year'] = df['Date'].dt.year

df_2016 = df[df['Year'] == 2016]

missing_data = df_2016.isna().any(axis=1).sum()
print('Missing datapoints :', missing_data)
#Missing datapoints: 1

df_clean = df_2016.dropna()

hourly_counts = df_clean.groupby('Hour')['sum'].sum()

plt.plot(hourly_counts.index, hourly_counts.values)
plt.xlabel('Hour of the day')
plt.ylabel('Total daily counts')
plt.title('Bicycle counts by hour in 2016')
plt.savefig('counts_by_hour.png')
plt.plot()

hourly_average = df_clean.groupby('Hour')['sum'].mean()

busiest_hour = hourly_average.index[np.argmax(hourly_average)]
print('Busiest hour is: ', busiest_hour)
#Busiest hour is:  17