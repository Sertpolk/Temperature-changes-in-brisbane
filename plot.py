import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# read data, remove columns we don't need, and remove any NaNs
data = pd.read_csv("tmax.040842.daily.csv",delimiter=",")
for title in data.columns.values:
    if not (title == "date" or title == "maximum temperature (degC)"):
        data = data.drop(title, 1)
data = data.dropna()

# create date objects instead of things like 2/03/1999 that look like dates but are actually strings
dates = pd.to_datetime(data['date'], dayfirst = True)

# plot data
plt.title("Brisbane Maximum Daily Temperatures")
plt.ylabel("Maximum Temperature (degC)")
plt.xlabel("Date")
plt.set_cmap('plasma')

plt.plot(dates, data['maximum temperature (degC)'],',r')
#plt.show()
plt.savefig("raw_maximum_temperature_graph.png")

