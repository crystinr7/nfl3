import main
import csv
import functools
import grabAttributes
import analyzeAndTrain

indices = []
numOfAttrs = 15
xgivenwin = []
notxgivenwin = []
list = []


def getNumOfGames():
    i = 0
    with open(dataset, 'r') as r:
        read = csv.reader(r, delimiter=' ', quotechar=',')
        for _ in read:
            i += 1
    return i

def p_x_y(attr):
    with open(dataset, 'r') as csvfile:
        next(csvfile)
        read = csv.reader(csvfile, delimiter=' ', quotechar=',')
        given_win = 0
        given_loss = 0
        notxgivenwin = 0
        notxgivenloss = 0
        for row in read:
            # This grabs a certain column and reads how many times it happens
            for word in row:

                word = word.split(",")

                for i in range(len(row)): #

                    if '1' in word[attr] and '1' in word[-1]:
                        given_win += 1
                    if '1' in word[attr] and '0' in word[-1]:
                        given_loss += 1
                    if '0' in word[attr] and '1' in word[-1]:
                        notxgivenwin += 1
                    if '0' in word[attr] and '0' in word[-1]:
                        notxgivenloss += 1

        p_not_x_y = given_loss / numOfGames
        p_x_y = given_win / numOfGames
        not_p_x_y = notxgivenwin / numOfGames
        not_p_not_x_y = notxgivenloss / numOfGames

    return p_x_y, not_p_x_y

def prob_of_win():
    return 0.5
def prob_of_lose():
    return 0.5
def all_indices(value, list):

    idx = -1
    while True:
        try:
            idx = list.index(value, idx+1)
            indices.append(idx)
        except ValueError:
            break
    return indices

def train():
    answer = []

    for i in range(numOfAttrs):
        xgivenwin.append(p_x_y(i)[0])
        notxgivenwin.append(p_x_y(i)[1])

    prob_x_win = functools.reduce(lambda x, y: x * y if y != 0 and x != 0 else 0.1, xgivenwin) * prob_of_win()
    prob_not_x_win = functools.reduce(lambda x, y: x * y if y != 0 and x != 0 else 0.1, notxgivenwin) * prob_of_win()

    answer.append(prob_x_win)
    answer.append(prob_not_x_win)
    print(answer)
    return prob_x_win





def dataset(num):
    if num == 0:
        return "trainingdata1.csv"
    if num == 1:
        return "trainingdata2.csv"

dataset = dataset(0)
numOfGames = getNumOfGames()
for i in range(numOfAttrs):
    xgivenwin.append(p_x_y(i)[0])
    notxgivenwin.append(p_x_y(i)[1])

#for row in dataset(0):

#train()

