import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
import datetime

plot_raw = False
plot_line = False
plot_quadratic = False
plot_smoothed = True

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
    line_fit = np.polyfit(x, y, 1)
    average_line = np.poly1d(line_fit)
    plt.ylim((22, 28))

    plt.plot(dates, data['maximum temperature (degC)'],',r')
    plt.plot(dates, average_line(x), '-k')
    #plt.show()
    plt.savefig("raw_maximum_temperature_graph_with_line.png")

if plot_quadratic:
    # plot a quadratic on the data
    plt.figure(3)
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
    # plt.savefig("raw_maximum_temperature_graph_with_quadratic.png")

# function to smooth the temperature data
def smooth_data(temperatures, window):
    return np.convolve(temperatures, np.ones(window) / window, 'same')

def data_for_year(dates, temperatures, yr):
    if len(dates) != len(temperatures):
        sys.stderr.write("Length of dates (" + str(len(dates)) + ") which is not equal to length of temperatures (" + str(len(temperatures)) + ")\n")
        sys.exit(1)
    start_time = datetime.date(yr, 1, 1)
    end_time = datetime.date(yr + 1, 1, 1)
    return [temperatures[i] for i in range(len(temperatures)) if (dates.iloc[i] >= start_time and dates.iloc[i] < end_time)]

if plot_smoothed:
    # plot a quadratic on the data
    plt.figure(4)
    plt.title("Brisbane Maximum Daily Temperatures")
    plt.ylabel("Smoothed Maximum Temperature (degC)")
    plt.xlabel("Day in year")
    plt.set_cmap('plasma')

    plt.plot(data_for_year(dates, smooth_data(data['maximum temperature (degC)'], 30), 1957))
    plt.plot(data_for_year(dates, smooth_data(data['maximum temperature (degC)'], 30), 2018))
    plt.show()
