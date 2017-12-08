import matplotlib.pyplot as plt



# x-coordinates of left sides of bars
left = [1, 3, 5]

# heights of bars
height = [11, 14, 13]

# labels for bars
tick_label = ['Naive Bayes', "Feature Selection", 'Weighted Features']

# plotting a bar chart
plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=['red', 'green'])

plt.ylim(0,16)
plt.xlim(0,6)
# naming the x-axis
plt.xlabel('Games up to week 11')
# naming the y-axis
plt.ylabel('16 Games')
# plot title
plt.title('Week 12 Prediction Accuracy')

# function to show the plot
plt.show()
# x-coordinates of left sides of bars
left = [1, 3, 5]

# heights of bars
height = [9, 13, 12]

# labels for bars
tick_label = ["NB Spread", "FS Spread", 'WF Spread']

# plotting a bar chart
plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=['red', 'green'])
# setting x and y axis range
plt.ylim(0,16)
plt.xlim(0,6)
# naming the x-axis
plt.xlabel('Games up to week 11')
# naming the y-axis
plt.ylabel('16 Games')
# plot title
plt.title('Week 12 Prediction Accuracy')

# function to show the plot
plt.show()