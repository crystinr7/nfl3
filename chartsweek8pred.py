import matplotlib.pyplot as plt

# x-coordinates of left sides of bars
left = [13, 14, 15]

# heights of bars
height = [11, 12, 12]

# labels for bars
tick_label = ['Naive Bayes', "Feature Selection", 'Weighted Features']

# plotting a bar chart
plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=['red', 'green', 'green'])

# naming the x-axis
plt.xlabel('Games up to week 7')
# naming the y-axis
plt.ylabel('13 Games')
# plot title
plt.title('Week 8 Prediction Accuracy')

# function to show the plot
plt.show()

# x-coordinates of left sides of bars
left = [13, 14, 15]

# heights of bars
height = [6, 9, 8]

# labels for bars
tick_label = ['Naive Bayes', "Feature Selection", 'Weighted Features']

# plotting a bar chart
plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=['red', 'green'])

# naming the x-axis
plt.xlabel('Games up to week 7')
# naming the y-axis
plt.ylabel('13 Games')
# plot title
plt.title('Week 8 Prediction Accuracy')

# function to show the plot
plt.show()

