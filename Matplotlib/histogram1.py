# A histogram is a graph showing frequency distributions.
# It is a graph showing the number of observations within each given interval.
import matplotlib.pyplot as plt
height = [125, 146, 120, 132, 154, 167, 178, 154, 167, 168, 112, 132, 134, 148, 138, 162, 147,
          123, 135, 126, 148, 126, 144, 120, 147, 146, 132, 136, 138, 136, 158, 149, 150, 143, 148, 146]
plt.hist(height, bins=10, color='red')
plt.title('Frequency Table of Height(student)')
plt.xlabel('Height in cm')
plt.ylabel('No. of students')
plt.savefig('hostogram.png')
plt.show()
