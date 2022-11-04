import matplotlib.pyplot as plt
import numpy as np
cities = ['dehli', 'mumbai', 'noida', 'ghaziabad']
rainfall = [10, 20, 30, 40]
humidity = [8, 14, 23, 34]
aqi = [28, 34, 53, 12]
# this is compulsory to seperate bars from each other
x = np.arange(len(cities))
print(x)
plt.bar(cities, rainfall, width=0.15)
plt.bar(x+.15, humidity, width=0.15)
plt.bar(x+0.30, aqi, width=0.15)
plt.title('Rainfall in NCR')
plt.xlabel('Cities')
plt.legend(('rainfall', 'humidity', 'AQI'))
plt.grid(True)
plt.show()
