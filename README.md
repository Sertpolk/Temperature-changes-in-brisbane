# Temperature Changes In Brisbane

We are investigating the temperature changes in Brisbane over the past years.  We are not trying to prove *global* climate change.  We are also not trying to explain *why* any changes occurred.  We are simply exploring the temperature data for Brisbane.

# Data Source:

We got the data from: bom.gov.au/climate/data/acorn-sat on Monday 2 March 2020.  This is a daily data series, starting on 4 June 1949 and ending on 31 May 2019: almost 71 years.

# Maximum Temperature

The following analysis is for the maximum daily temperature recorded at Brisbane airport.  You can do the analysis yourself with the `plot.py` python script.

## Max temperature: raw data visualisation:

This is what our data looks like: 

![Image](raw_maximum_temperature_graph.png)

## Max temperature: fitting a straight line:

If we fit a straight line to the data we can see if the general trend is increasing or decreasing. 
The following graph shows that over the past 71 years, the temperature at Brisbane airport has most likely increased.  
At this stage we cannot really say "it has definitely increased by 0.75 degC" because there is a lot of scatter in the temperature data.  
But it certainly looks like Brisbane airport has got hotter.

![Image](raw_maximum_temperature_graph_with_line.png)

## Max temperature: fitting a quadratic to the graph

If we fit a quadratic to the data we can see if the general trend is increasing or decreasing. 
The following graph shows that over the past 71 years, the temperature at Brisbane airport has most likely increased.  
At this stage we cannot really say "it has definitely increased by 0.6 degC" because there is a lot of scatter in the temperature data.  
But it certainly looks like Brisbane airport has got hotter.

![Image](raw_maximum_temperature_graph_with_quadratic.png)

## Max temperature: inspecting one year of data

Maybe the temperature increase is because:

- the winters are getting warmer, or
- the summers are getting warmer, or
- all seasons are getting warmer.

Or maybe something else!  To explore this idea, we can compare the temperature for two years, say 1950 and 2018.  But when we do this, we see a lot of scatter in the data and it's hard to pick out a pattern.

Therefore, we plot *smoothed* data.  Our strategy is to perform a "running mean".  For instance, we could set "the temperature on Wednesday" to be the average of the measured temperatures on Monday, Tuesday, Wednesday, Thursday and Friday.   More generally, to get the temperature on a single day, we average over a number of days in its immediate past, and a number of days in its immediate future.  The bigger the "number of days", the smoother the result.

The figure below shows various smoothed temperature curves for the year 1950.

![Image](raw_maximum_temperature_graph_with_smoothed_1950_data.png)

If we plot the running mean for 1950 and 2018, we can see the smoothed data.  There is quite a lot of "wigglyness" here, and maybe 1950 and 2018 are "special" for some reason, so instead, let's explore the temperature changes by decade.

![Image](raw_maximum_temperature_smoothed_graph_1950_and_2018.png)

## Max temperature: through the decades

In the graph below, we plot the annual temperatures in each decade.  We do this by:

1. Smoothing the entire data with the "running mean" idea used above.  We use a window of 50 days.
2. To get the temperature on 1 Jan for the 1950s, we average the temperature on 1 Jan 1950, 1 Jan 1951, 1 Jan 1952, ..., 1 Jan 1959.  To get the temperature on the 2 Jan for the 1950s, we average the temperature on 2 Jan 1950, 2 Jan 1951, ..., 2 Jan 1959.  And so on.
3. We do this for each decade: 1950s, 1960s, 1970s, ... 2010s.  (There is no data for 2019, so we only use 2010, 2011, 2012, ..., 2019 for the 2010s series.)
4. We plot the data

It looks like the maximum temperatures have mostly increased in the winter and spring, and there's less obvious change in the summer and autumn.

![Image](max_decades.png)


# Minimum Temperature

The following analysis is for the minimum daily temperature recorded at Brisbane airport.  You can do the analysis yourself with the `plot_min.py` python script.

## Min temperature: raw data visualisation:

This is what our data looks like: 

![Image](raw_minimum_temperature_graph.png)

## Min temperature: fitting a straight line:

If we fit a straight line to the data we can see if the general trend is increasing or decreasing. 
The following graph shows that over the past 71 years, the temperature at Brisbane airport has most likely increased.  
At this stage we cannot really say "it has definitely increased by 1.4 degC" because there is a lot of scatter in the temperature data.  
But it certainly looks like Brisbane airport has got hotter.

![Image](raw_minimum_temperature_graph_with_line.png)

## Min temperature: fitting a quadratic to the graph

If we fit a quadratic to the data we can see if the general trend is increasing or decreasing. 
The following graph shows that over the past 71 years, the temperature at Brisbane airport has most likely increased.  
At this stage we cannot really say "it has definitely increased by 1.6 degC" because there is a lot of scatter in the temperature data.  
But it certainly looks like Brisbane airport has got hotter.

![Image](raw_minimum_temperature_graph_with_quadratic.png)

## Min temperature: inspecting one year of data

Maybe the temperature increase is because:

- the winters are getting warmer, or
- the summers are getting warmer, or
- all seasons are getting warmer.

Or maybe something else!  To explore this idea, we can compare the temperature for two years, say 1950 and 2018.  But when we do this, we see a lot of scatter in the data and it's hard to pick out a pattern.

Therefore, we plot *smoothed* data.  Our strategy is to perform a "running mean".  For instance, we could set "the temperature on Wednesday" to be the average of the measured temperatures on Monday, Tuesday, Wednesday, Thursday and Friday.   More generally, to get the temperature on a single day, we average over a number of days in its immediate past, and a number of days in its immediate future.  The bigger the "number of days", the smoother the result.

The figure below shows various smoothed temperature curves for the year 1950.

![Image](raw_minimum_temperature_graph_with_smoothed_1950_data.png)

If we plot the running mean for 1950 and 2018, we can see the smoothed data.  There is quite a lot of "wigglyness" here, and maybe 1950 and 2018 are "special" for some reason, so instead, let's explore the temperature changes by decade.

![Image](raw_minimum_temperature_smoothed_graph_1950_and_2018.png)

## Min temperature: through the decades

In the graph below, we plot the annual temperatures in each decade.  We do this by:

1. Smoothing the entire data with the "running mean" idea used above.  We use a window of 50 days.
2. To get the temperature on 1 Jan for the 1950s, we average the temperature on 1 Jan 1950, 1 Jan 1951, 1 Jan 1952, ..., 1 Jan 1959.  To get the temperature on the 2 Jan for the 1950s, we average the temperature on 2 Jan 1950, 2 Jan 1951, ..., 2 Jan 1959.  And so on.
3. We do this for each decade: 1950s, 1960s, 1970s, ... 2010s.  (There is no data for 2019, so we only use 2010, 2011, 2012, ..., 2019 for the 2010s series.)
4. We plot the data

It looks like the minimum temperatures have increased throughout most of the year!

![Image](min_decades.png)

