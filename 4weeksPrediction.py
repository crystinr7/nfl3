import matplotlib.pyplot as plt

# line 1 points
x1 = [8, 9, 12, 13]
y1 = [84.615, 53.84, 68.75, 56.25]
# plotting the line 1 points
plt.plot(x1, y1, label="Outcome")
plt.ylim(0,100)
plt.xlim(8,13)
# line 2 points
x2 = [8, 9, 12, 13]
y2 = [61.53, 76.69, 56.25, 62.5]
# plotting the line 2 points
plt.plot(x2, y2, label="Spread")

# naming the x axis
plt.xlabel('Week 8, 9, 13')
# naming the y axis
plt.ylabel('Each Week')
# giving a title to my graph
plt.title('4 Weeks of Predictions - Naive Bayes!naivefff›')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()


# line 1 points
x1 = [8, 9, 12, 13]
y1 = [92.3, 69.23, 87.5, 56.25]
# plotting the line 1 points
plt.plot(x1, y1, label="Outcome")
plt.ylim(0,100)
plt.xlim(8,13)
# line 2 points
x2 = [8, 9, 12, 13]
y2 = [69.23, 61.53, 81.25, 62.5]
# plotting the line 2 points
plt.plot(x2, y2, label="Spread")

# naming the x axis
plt.xlabel('Week 8, 9, 12, 13')
# naming the y axis
plt.ylabel('Each Week')
# giving a title to my graph
plt.title('4 Weeks of Prediction - Feature Selection')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()

# line 1 points
x1 = [8, 9, 12, 13]
y1 = [92.3, 84.61, 81.25, 62.5]
# plotting the line 1 points
plt.plot(x1, y1, label="Outcome")
plt.ylim(0,100)
plt.xlim(8,13)
# line 2 points
x2 = [8, 9, 12, 13]
y2 = [69.23, 92.23, 75, 62.5]
# plotting the line 2 points
plt.plot(x2, y2, label="Spread")
# setting x and y axis range

# naming the x axis
plt.xlabel('Week 8, 9, 12, 13')
# naming the y axis
plt.ylabel('Each Week')
# giving a title to my graph
plt.title('4 Weeks of Predictions - Weighted Features')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()

import matplotlib.pyplot as plt

# line 1 points
x1 = [1, 2, 3, 1]
y1 = [2, 4, 1, 1]
# plotting the line 1 points
plt.plot(x1, y1, label="Naive Bayes")

# line 2 points
x2 = [1, 2, 3, 1]
y2 = [4, 1, 3, 1]
# plotting the line 2 points
plt.plot(x2, y2, label="Feature Selection")

# line 3 points
x3 = [1, 2, 3, 1]
y3 = [4, 1, 3, 1]
# plotting the line 2 points
plt.plot(x3, y3, label="Weighted Features")
# naming the x axis
plt.xlabel('4 weeks of predictions')
# naming the y axis
plt.ylabel('Accuracy')
# giving a title to my graph
plt.title('Accuracy according to week')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()