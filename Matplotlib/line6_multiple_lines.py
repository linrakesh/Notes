from turtle import width
import matplotlib.pyplot as plt
cities = ['dehli', 'mumbai', 'noida', 'ghaziabad']
rainfall = [10, 20, 30, 40]
humidity = [12, 34, 16, 52]
# for adding legeds either put label in plot for each line
plt.plot(cities, rainfall, marker="h")
plt.plot(cities, humidity, marker='H')
plt.title('Rainfall + Humidity Chart in NCR')
plt.xlabel('NCR Cities')
#loc is optional - 'upper left','upper right'
# put legends first parameter in the form of a tuple - all elements string
plt.legend(('rainfall', 'humidify'), loc="upper right")
plt.grid(True)
plt.show()
