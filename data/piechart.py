# # of men with medals: 410
## of women with medals: 243
import matplotlib.pyplot as plt 

values = [410, 243]
labels = ["Men", "Women"]
colors =  ["steelblue", "gold"]
explode = (0, 0.1)

plt.pie (values, labels=labels, colors=colors, explode=explode)
plt.show()