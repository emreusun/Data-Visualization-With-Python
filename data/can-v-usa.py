import matplotlib.pyplot as plt 

years = [1924, 2014]
medals = [0, 625]



# plot our chart with data above
plt.plot(years, medals,  color="red", linewidth=3.0)


medalsx = [0, 653]
plt.plot(years, medalsx, color="blue", linewidth=3.0)

# label on the left hand side
plt.ylabel("Medals")
#label on the bottom of the cart
plt.xlabel("Country")

#add a title to the chart
plt.title("Canada vs Usa medal chart", pad="22")

plt.legend(["CAN", "USA" ])
# run the show method (this lives inside the pyplot package)
# this will generate a graph in a new window
plt.show()