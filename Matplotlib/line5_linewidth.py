from turtle import width
import matplotlib.pyplot as plt
# optional parameter

# color - blue,green,red,magenta,yellow,black
# linewidth - it is in points
# linestyle - 'solid','dashed','dashdot','dotted'
# marker - '.' , ',' ,'o','+','D','d','s','p','*','h','H'
# markersize - again in point
# markeredgecolor- again the same color code

plt.plot(['dehli', 'mumbai', 'noida', 'ghaziabad'],
         [10, 20, 30, 40], color='green', marker="*",
         linewidth=3, linestyle="dashed")
plt.title('Rainfall in NCR')
plt.xlabel('NCR Cities')
plt.ylabel('rainfall in mm')
# grid method activates the grid in output
plt.grid(True)
plt.show()
