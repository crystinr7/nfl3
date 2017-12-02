import math


# Z = normalization factor
z = []

alpha = []
# Distribution
D = []
# Hypothesis
h = []
m = 30
y = [0,1]

# ERROR
epsilon = []
# REFER TO SLIDES BOOSTING
D[0] = 1 / m
for i in z:
    z[i] = math.sum(D(i)*math.e^{-alpha[i]*y[i]*h[i]})
for i in D[1:m]:
        D[i+1] = (D[i]/z[i])* math.e^{-alpha[i]*y[i]*h[i]}
for i in alpha:
    alpha[i] = 1/2*math.log((1-epsilon[i])/epsilon[i], 2)