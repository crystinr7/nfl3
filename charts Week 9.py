import matplotlib.pyplot as plt



# x-coordinates of left sides of bars
left = [1, 3, 6, 8, 10, 12]

# heights of bars
height = [6, 6, 7, 7, 8, 6]

# labels for bars
tick_label = ['NB', "NB Spread", "FS", "FS Spread", 'WF', "WF Spread"]

# plotting a bar chart
plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=['red', 'green'])

# naming the x-axis
plt.xlabel('Games up to week 8')
# naming the y-axis
plt.ylabel('13 Games')
# plot title
plt.title('Week 8 Prediction Accuracy')

# function to show the plot
plt.show()