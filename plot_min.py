import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
import datetime
import matplotlib.colors as mcol
import matplotlib.cm as cm

plot_raw = False
plot_line = False
plot_quadratic = False
plot_smoothed = False
plot_1950_2018_smoothed = False
angry = False

# read data, remove columns we don't need, and remove any NaNs
data = pd.read_csv("tmin.040842.daily.csv",delimiter=",")
for title in data.columns.values:
    if not (title == "date" or title == "minimum temperature (degC)"):
        data = data.drop(title, 1)
data = data.dropna()

# create date objects instead of things like 2/03/1999 that look like dates but are actually strings
dates = pd.to_datetime(data['date'], dayfirst = True)

if plot_raw:
    # plot data
    plt.figure(1)
    plt.title("Brisbane Minimum Daily Temperatures")
    plt.ylabel("Minimum Temperature (degC)")
    plt.xlabel("Date")
    plt.set_cmap('plasma')

    plt.plot(dates, data['minimum temperature (degC)'],',b')
    plt.show()
    # plt.savefig("raw_minimum_temperature_graph.png")

if plot_line:
    # plot a line on the data
    plt.figure(2)
    plt.title("Brisbane Minimum Daily Temperatures")
    plt.ylabel("Minimum Temperature (degC)")
    plt.xlabel("Date")
    plt.set_cmap('plasma')

    y = data['minimum temperature (degC)']
    x = list(range(len(y)))
    line_fit = np.polyfit(x, y, 1)
    average_line = np.poly1d(line_fit)
    plt.ylim((11, 19))

    plt.plot(dates, data['minimum temperature (degC)'],',b')
    plt.plot(dates, average_line(x), '-k')
    plt.show()
    # plt.savefig("raw_minimum_temperature_graph_with_line.png")

if plot_quadratic:
    # plot a quadratic on the data
    plt.figure(3)
    plt.title("Brisbane Minimum Daily Temperatures")
    plt.ylabel("Minimum Temperature (degC)")
    plt.xlabel("Date")
    plt.set_cmap('plasma') 

    y = data['minimum temperature (degC)']
    x = list(range(len(y)))
    line_fit = np.polyfit(x, y, 2)
    average_line = np.poly1d(line_fit)
    plt.ylim((11, 19))

    plt.plot(dates, data['minimum temperature (degC)'],',b')
    plt.plot(dates, average_line(x), '-k')
    plt.show()
    # plt.savefig("raw_minimum_temperature_graph_with_quadratic.png")

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
    plt.title("Brisbane Minimum Daily Temperatures (1950)")
    plt.ylabel("Smoothed Minimum Temperature (degC)")
    plt.xlabel("Day in year")
    plt.set_cmap('plasma')

    plt.plot(data_for_year(dates, smooth_data(data['minimum temperature (degC)'], 5), 1950), label = '5 day smoothing')
    plt.plot(data_for_year(dates, smooth_data(data['minimum temperature (degC)'], 10), 1950), label = '10 day smoothing')
    plt.plot(data_for_year(dates, smooth_data(data['minimum temperature (degC)'], 20), 1950), label = '20 day smoothing')
    plt.plot(data_for_year(dates, smooth_data(data['minimum temperature (degC)'], 100), 1950), label = '100 day smoothing')
    plt.legend()
    plt.show()
    # plt.savefig("raw_minimum_temperature_graph_with_smoothed_1950_data.png")

if plot_1950_2018_smoothed:
    # plot a smoothed line on the data
    plt.figure(4)
    plt.title("Brisbane Minimum Daily Temperatures (1950 & 2018)")
    plt.ylabel("Smoothed Minimum Temperature (degC)")
    plt.xlabel("Day in year")
    plt.set_cmap('plasma')

    plt.plot(data_for_year(dates, smooth_data(data['minimum temperature (degC)'], 20), 1950), label = '20 day smoothing 1950')
    plt.plot(data_for_year(dates, smooth_data(data['minimum temperature (degC)'], 20), 2018), label = '20 day smoothing 2018')

    plt.legend()
    plt.show()
    # plt.savefig("raw_minimum_temperature_smoothed_graph_1950_and_2018.png")

def DecadeData(decade, smoothing):
    sd = smooth_data(data['minimum temperature (degC)'], smoothing)
    a1 = ((data_for_year(dates, sd, decade)))
    a2 = ((data_for_year(dates, sd, decade+1)))
    a3 = ((data_for_year(dates, sd, decade+2)))
    a4 = ((data_for_year(dates, sd, decade+3)))
    a5 = ((data_for_year(dates, sd, decade+4)))
    a6 = ((data_for_year(dates, sd, decade+5)))
    a7 = ((data_for_year(dates, sd, decade+6)))
    a8 = ((data_for_year(dates, sd, decade+7)))
    a9 = ((data_for_year(dates, sd, decade+8)))
    if decade <2008:
        a10 = ((data_for_year(dates, sd, decade+9)))
        m = min([len(a1), len(a2), len(a3), len(a4), len(a5), len(a6), len(a7), len(a8), len(a9), len(a10)])
        result = list(range(m))
        for day in range(m):
            result[day] = (a1[day] + a2[day] + a3[day] + a4[day] + a5[day] + a6[day] + a7[day] + a8[day] + a9[day] +
                           a10[day]) / 10.0
    else:
        m = min([len(a1), len(a2), len(a3), len(a4), len(a5), len(a6), len(a7), len(a8), len(a9)])
        result = list(range(m))
        for day in range(m):
            result[day] = (a1[day] + a2[day] + a3[day] + a4[day] + a5[day] + a6[day] + a7[day] + a8[day] + a9[day])/ 9.0
    return result



if angry:
    # Color stuff: https://stackoverflow.com/questions/25748183/python-making-color-bar-that-runs-from-red-to-blue
    # Make a user-defined colormap that will vary from blue to red
    cm1 = mcol.LinearSegmentedColormap.from_list("MyCmapName",["b", "r"])
    # Make a normalizer that will map the decade values
    # [1950, 2011] -> [0,1].
    cnorm = mcol.Normalize(vmin = 1950, vmax = 2010)
    # Turn these into an object that can be used to map time values to colors and
    # can be passed to plt.colorbar().
    cpick = cm.ScalarMappable(norm = cnorm, cmap = cm1)
    cpick.set_array([])
    
    sys.stdout.write("Plotting decade data\n")
    plt.figure(6)
    plt.title("Brisbane Minimum Daily Temperatures\nSmoothed and averaged by decade")
    plt.ylabel("Minimum Temperature (degC)")
    plt.xlabel("Day in year")
    plt.set_cmap('plasma')

    for dec in [1950, 1960, 1970, 1980, 1990, 2000, 2010]:
        sys.stdout.write(str(dec) + "\n")
        plt.plot(DecadeData(dec, 50), label = str(dec) + "s", color = cpick.to_rgba(dec))

    plt.legend()
    plt.show()
    #plt.savefig("min_decades.png")
