import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("tmax.040842.daily.csv",delimiter=",")

print(data['date'])
print(data['maximum temperature (degC)'])

dates = pd.to_datetime(data['date'])
plt.title("Brisbane Maximum Temperatures")
plt.xlabel("Maximum Temperature")
plt.ylabel("Date")
plt.set_cmap('plasma')

plt.plot(dates,data['maximum temperature (degC)'],',r')
plt.show()

