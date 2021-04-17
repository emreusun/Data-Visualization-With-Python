import numpy as np
import matplotlib.pyplot as plt 

labels=["CAN", "RUS", "KAZ"]
years = [1924, 2014]
medals = [9, 90]

x_years = np.arange(len(years))
width = 0.25 

# plot our chart with data above
plt.bar(x_years - width, medals,width=width,  color="red", )


medals2 = [13, 65]
plt.bar(x_years, medals2,width=width, color="cyan", )

medals3 = [17, 36]
plt.bar(x_years + width, medals3,width=width, color="orange", )



# label on the left hand side
plt.ylabel("Medals")
#label on the bottom of the cart
plt.xlabel("Years")
#add a title to the chart
plt.xticks(ticks=x_years, labels=years)

plt.title("Canada vs USA vs Norway Medal Chart comparison by years 1924-2014" , pad="22")

plt.legend(["CAN", "USA","NOR" ])
# run the show method (this lives inside the pyplot package)
# this will generate a graph in a new window

plt.tight_layout()

plt.show()