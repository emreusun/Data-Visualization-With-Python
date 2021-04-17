import matplotlib.pyplot as plt 

years = [1900, 1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015]
pops = [1.6, 2.5, 2.6, 3.0, 3.3, 3.6, 4.2, 4.4, 4.8, 5.3, 5.7, 6.1, 6.5, 6.9, 7.3]

# plot our chart with data above
plt.plot(years, pops)

# run the show method (this lives inside the pyplot package)
# this will generate a graph in a new window
plt.show()