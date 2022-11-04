import matplotlib.pyplot as plt
cities = ['dehli', 'mumbai', 'noida', 'ghaziabad']
rainfall = [10, 20, 30, 40]
humidity = [8, 14, 23, 34]
plt.bar(cities, rainfall)
plt.bar(cities, humidity)
plt.title('Rainfall in NCR')
plt.xlabel('Cities')
plt.ylabel('Rainfall(mm)')
plt.legend(('rainfall', 'humidity'))
plt.grid(True)
plt.show()
