import matplotlib.pyplot as plt
cities = ['dehli', 'mumbai', 'noida', 'ghaziabad']
rainfall = [10, 20, 30, 40]
plt.bar(cities, rainfall)
plt.title('Rainfall in NCR')
plt.xlabel('Cities')
plt.ylabel('Rainfall(mm)')
plt.grid(True)
plt.show()
