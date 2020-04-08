# Temperature Changes In Brisbane

We are investigating the temperature changes in Brisbane over the past years.  We are not trying to prove *global* climate change.  We are also not trying to explain *why* any changes occurred.  We are simply exploring the temperature data for Brisbane.

## Data Source:

We got the data from: bom.gov.au/climate/data/acorn-sat on Monday 2 March 2020.  This is a daily data series, starting on 4 June 1949 and ending on 31 May 2019: almost 71 years.

## Raw Data Visualisation:

This is what our data looks like: 

![Image](raw_maximum_temperature_graph.png)

## Fitting a straight line:

If we fit a straight line to the data we can see if the general trend is increasing or decreasing. 
The following graph shows that over the past 71 years, the temperature at Brisbane airport has most likely increased.  
At this stage we cannot really say "it has definitely increased by 0.75 degC" because there is a lot of scatter in the temperature data.  
But it certainly looks like Brisbane airport has got hotter.

![Image](raw_maximum_temperature_graph_with_line.png)

## Fitting a quadratic to the graph

If we fit a quadratic to the data we can see if the general trend is increasing or decreasing. 
The following graph shows that over the past 71 years, the temperature at Brisbane airport has most likely increased.  
At this stage we cannot really say "it has definitely increased by 0.6deg C" because there is a lot of scatter in the temperature data.  
But it certainly looks like Brisbane airport has got hotter.

![Image](raw_maximum_temperature_graph_with_quadratic.png)

## Inspecting one year of data

Maybe the temperature increase is because:

- the winters are getting warmer, or
- the summers are getting warmer, or
- all seasons are getting warmer.

Or maybe something else!  To explore this idea, we can compare the temperature for two years, say 1950 and 2018.  But when we do this, we see a lot of scatter in the data and it's hard to pick out a pattern.

Therefore, we plot *smoothed* data.  Our strategy is to perform a "running mean".  For instance, we could set "the temperature on Wednesday" to be the average of the measured temperatures on Monday, Tuesday, Wednesday, Thursday and Friday.   More generally, to get the temperature on a single day, we average over a number of days in its immediate past, and a number of days in its immediate future.  The bigger the "number of days", the smoother the result.

The figure below shows various smoothed temperature curves for the year 1950.

![Image](raw_maximum_temperature_graph_with_smoothed_1950_data.png)

If we plot the running mean for 1950 and 2018, we can see the smoothed data.

![Image](raw_maximum_temperature_smoothed_graph_1950_and_2018.png)
