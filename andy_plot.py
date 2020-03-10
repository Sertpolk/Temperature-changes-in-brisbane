import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("tmax.040842.daily.csv",delimiter=",")
for col_name in data.columns:
    if col_name == "date" or col_name == "maximum temperature (degC)":
        continue
    data = data.drop(col_name, 1)
data = data.dropna()

dates = pd.to_datetime(data['date'])

plt.plot(dates, data['maximum temperature (degC)'])
plt.show()
