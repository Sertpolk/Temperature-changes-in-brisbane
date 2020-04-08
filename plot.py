import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
import datetime

plot_raw = False
plot_line = False
plot_quadratic = False
plot_smoothed = False
plot_1950_2018_smoothed = False
E = True

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
    # plot a smoothed line on the data
    plt.figure(4)
    plt.title("Brisbane Maximum Daily Temperatures (1950)")
    plt.ylabel("Smoothed Maximum Temperature (degC)")
    plt.xlabel("Day in year")
    plt.set_cmap('plasma')

    plt.plot(data_for_year(dates, smooth_data(data['maximum temperature (degC)'], 5), 1950), label = '5 day smoothing')
    plt.plot(data_for_year(dates, smooth_data(data['maximum temperature (degC)'], 10), 1950), label = '10 day smoothing')
    plt.plot(data_for_year(dates, smooth_data(data['maximum temperature (degC)'], 20), 1950), label = '20 day smoothing')
    plt.plot(data_for_year(dates, smooth_data(data['maximum temperature (degC)'], 100), 1950), label = '100 day smoothing')
    plt.legend()
    plt.show()

if plot_1950_2018_smoothed:
    # plot a smoothed line on the data
    plt.figure(4)
    plt.title("Brisbane Maximum Daily Temperatures (1950 & 2018)")
    plt.ylabel("Smoothed Maximum Temperature (degC)")
    plt.xlabel("Day in year")
    plt.set_cmap('plasma')

    plt.plot(data_for_year(dates, smooth_data(data['maximum temperature (degC)'], 20), 1950), label = '20 day smoothing 1950')
    plt.plot(data_for_year(dates, smooth_data(data['maximum temperature (degC)'], 20), 2018), label = '20 day smoothing 2018')

    plt.legend()
    plt.show()
    # plt.savefig("raw_maximum_temperature_smoothed_graph_1950_and_2018.png")

if plot_smoothed:
    # plot a smoothed line on the data
    plt.figure(4)
    plt.title("Brisbane Maximum Daily Temperatures (1950)")
    plt.ylabel("Smoothed Maximum Temperature (degC)")
    plt.xlabel("Day in year")
    plt.set_cmap('plasma')

    plt.plot(data_for_year(dates, smooth_data(data['maximum temperature (degC)'], 5), 1950), label = '5 day smoothing')
    plt.plot(data_for_year(dates, smooth_data(data['maximum temperature (degC)'], 10), 1950), label = '10 day smoothing')
    plt.plot(data_for_year(dates, smooth_data(data['maximum temperature (degC)'], 20), 1950), label = '20 day smoothing')
    plt.plot(data_for_year(dates, smooth_data(data['maximum temperature (degC)'], 100), 1950), label = '100 day smoothing')
    plt.legend()
    plt.show()

def DecadeData(decade, smoothing):
    sd = smooth_data(data['maximum temperature (degC)'], smoothing)
    a1 = ((data_for_year(dates, sd, decade)))
    a2 = ((data_for_year(dates, sd, decade+1)))
    a3 = ((data_for_year(dates, sd, decade+2)))
    a4 = ((data_for_year(dates, sd, decade+3)))
    a5 = ((data_for_year(dates, sd, decade+4)))
    a6 = ((data_for_year(dates, sd, decade+5)))
    a7 = ((data_for_year(dates, sd, decade+6)))
    a8 = ((data_for_year(dates, sd, decade+7)))
    if decade <2008:
        a9 = ((data_for_year(dates, sd, decade+8)))
        a10 = ((data_for_year(dates, sd, decade+9)))
        m = min([len(a1), len(a2), len(a3), len(a4), len(a5), len(a6), len(a7), len(a8), len(a9), len(a10)])
        result = list(range(m))
        for day in range(m):
            result[day] = (a1[day] + a2[day] + a3[day] + a4[day] + a5[day] + a6[day] + a7[day] + a8[day] + a9[day] +
                           a10[day]) / 10.0
    else:
        m = min([len(a1), len(a2), len(a3), len(a4), len(a5), len(a6), len(a7), len(a8)])
        result = list(range(m))
        for day in range(m):
            result[day] = (a1[day] + a2[day] + a3[day] + a4[day] + a5[day] + a6[day] + a7[day] + a8[day])/ 8.0
    return result


if E:
    plt.figure(6)
    plt.title("Brisbane Maximum Daily Temperatures (1950 & 2018)")
    plt.ylabel("Smoothed Maximum Temperature (degC)")
    plt.xlabel("Day in year")
    plt.set_cmap('plasma')

    plt.plot(DecadeData(1950, 30), label = '1950s')
    plt.plot(DecadeData(1960, 30), label = '1960s')
    plt.plot(DecadeData(1970, 30), label = '1970s')
    plt.plot(DecadeData(1980, 30), label = '1980s')
    plt.plot(DecadeData(1990, 30), label = '1990s')
    plt.plot(DecadeData(2000, 30), label = '2000s')
    plt.plot(DecadeData(2010, 30), label = '2010s')

    plt.legend()
    plt.show()
