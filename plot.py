import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("tmax.040842.daily.csv",delimiter=",")

print(data['date'])
print(data['maximum temperature (degC)'])

plt.plot(data.index,data['maximum temperature (degC)'])
plt.show()
