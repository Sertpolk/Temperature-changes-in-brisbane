import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plot_raw = False
plot_line = True

# read data, remove columns we don't need, and remove any NaNs
data = pd.read_csv("tmax.040842.daily.csv",delimiter=",")
for title in data.columns.values:
    if not (title == "date" or title == "maximum temperature (degC)"):
        data = data.drop(title, 1)
data = data.dropna()

# create date objects instead of things like 2/03/1999 that look like dates but are actually strings
dates = pd.to_datetime(data['date'], dayfirst = True)

if plot_raw:
    # plot data
    plt.figure(1)
    plt.title("Brisbane Maximum Daily Temperatures")
    plt.ylabel("Maximum Temperature (degC)")
    plt.xlabel("Date")
    plt.set_cmap('plasma')

    plt.plot(dates, data['maximum temperature (degC)'],',r')
    #plt.show()
    plt.savefig("raw_maximum_temperature_graph.png")

if plot_line:
    # plot a line on the data
    plt.figure(2)
    plt.title("Brisbane Maximum Daily Temperatures")
    plt.ylabel("Maximum Temperature (degC)")
    plt.xlabel("Date")
    plt.set_cmap('plasma')

    y = data['maximum temperature (degC)']
    x = list(range(len(y)))
    line_fit = np.polyfit(x, y, 2)
    average_line = np.poly1d(line_fit)
    plt.ylim((22, 28))

    plt.plot(dates, data['maximum temperature (degC)'],',r')
    plt.plot(dates, average_line(x), '-k')
    plt.show()
    #plt.savefig("raw_maximum_temperature_graph_with_line.png")
