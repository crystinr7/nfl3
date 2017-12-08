import matplotlib.pyplot as plt



# x-coordinates of left sides of bars
left = [1, 3, 5]

# heights of bars
height = [38, 43, 46]

# labels for bars
tick_label = ['NB', "FS", 'WF']

# plotting a bar chart
plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=['red', 'green'])
plt.ylim(0,58)
plt.xlim(0,6)
# naming the x-axis
plt.xlabel('Accuracy Tested')
# naming the y-axis
plt.ylabel('58 Games')
# plot title
plt.title('Overall Accuracy')

# function to show the plot
plt.show()
# x-coordinates of left sides of bars
left = [1, 3, 5]

# heights of bars
height = [37, 40, 43]

# labels for bars
tick_label = ["NB Spread", "FS Spread", 'WF Spread']

# plotting a bar chart
plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=['red', 'green'])
plt.ylim(0,58)
plt.xlim(0,6)
# naming the x-axis
plt.xlabel('Tested Accuracy')
# naming the y-axis
plt.ylabel('58 Games')
# plot title
plt.title('Overall Accuracy')

# function to show the plot
plt.show()

# x-coordinates of left sides of bars
left = [1, 3, 5]

# heights of bars
height = [65.517, 68.96, 74.137]

# labels for bars
tick_label = ['NB', "FS", 'WF']

# plotting a bar chart
plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=['red', 'green'])
plt.ylim(0,100)
plt.xlim(0,6)
# naming the x-axis
plt.xlabel('Accuracy Tested')
# naming the y-axis
plt.ylabel('Percentage')
# plot title
plt.title('Overall Accuracy')

# function to show the plot
plt.show()
# x-coordinates of left sides of bars
left = [1, 3, 5]

# heights of bars
height = [63.673, 68.965, 74.137]

# labels for bars
tick_label = ["NB Spread", "FS Spread", 'WF Spread']

# plotting a bar chart
plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=['red', 'green'])
plt.ylim(0,100)
plt.xlim(0,6)
# naming the x-axis
plt.xlabel('Tested Accuracy')
# naming the y-axis
plt.ylabel('Percentage')
# plot title
plt.title('Overall Accuracy')

# function to show the plot
plt.show()
