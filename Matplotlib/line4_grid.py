import matplotlib.pyplot as plt
plt.plot(['dehli', 'mumbai', 'noida', 'ghaziabad'], [10, 20, 30, 40], )
plt.title('Rainfall in NCR')
plt.xlabel('NCR Cities')
plt.ylabel('rainfall in mm')
# grid method activates the grid in output
plt.grid(True)
plt.show()
