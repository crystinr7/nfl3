import requests
import csv
from bs4 import BeautifulSoup
import main



# LISTS FOR PROGRAM
players = []
totalmax = []
maxnumber = []
maxTeam = []

pOfXsWins = []
pOfXsLosses = []
probs_win = []
probs_lose = []

outcome = []
prob_t1_win = []
prob_t2_win = []

# Attribute lists

team1list = []
team2list = []
probabilities = []
winner_is = []
points = []
less_likely_to_lose = []
train_team_1_list = []
train_team_2_list = []

train_stats = []



def createTrainingCSV(team):
    with open(team, 'w') as c:
        writer = csv.writer(c, delimiter=' ',
                            quotechar=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow("Training Data")



def appendCSV(team):
    with open(team, "a") as f:
        wr = csv.writer(f)
        if winning_team() == 1:
            wr.writerow(train_team_1_list)
        else:
            wr.writerow(train_team_2_list)





def yearstatsForTeam1WIN():
    if winning_team() == 1:
        run_training_attrs()


def yearstatsForTeam2WIN():
    if winning_team() == 2:
        run_training_attrs()


# NAME OF EACH TEAM
def team1():
    return train_stats[0]


def team2():
    return train_stats[6]


# RETURNS WINNING TEAM FOR THAT GAME
def winning_team():
    if float(train_stats[5]) > float(train_stats[11]):
        return 1
    else:
        return 2



def train_attr1():
    # Grabs first quarter points
    if float(train_stats[1]) > float(train_stats[7]):

        train_team_1_list.append(1)
        train_team_2_list.append(0)
    elif float(train_stats[1]) == float(train_stats[7]):
        train_team_1_list.append(0.5)
        train_team_2_list.append(0.5)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


def train_attr2():
    # Grabs second quarter points
    if float(train_stats[2]) > float(train_stats[8]):
        train_team_1_list.append(1)
        train_team_2_list.append(0)
    elif float(train_stats[2]) == float(train_stats[8]):
        train_team_1_list.append(0.5)
        train_team_2_list.append(0.5)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


def train_attr3():
    # Grabs third quarter points
    if float(train_stats[3]) > float(train_stats[9]):
        train_team_1_list.append(1)
        train_team_2_list.append(0)
    elif float(train_stats[3]) == float(train_stats[9]):
        train_team_1_list.append(0.5)
        train_team_2_list.append(0.5)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


def train_attr4():
    if float(train_stats[4]) > float(train_stats[10]):
        train_team_1_list.append(1)
        train_team_2_list.append(0)
    elif float(train_stats[4]) == float(train_stats[10]):
        train_team_1_list.append(0.5)
        train_team_2_list.append(0.5)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


def train_attr5():
    # Grabs first downs
    if float(train_stats[13]) > float(train_stats[14]):
        train_team_1_list.append(1)
        train_team_2_list.append(0)
    elif float(train_stats[13]) == float(train_stats[14]):
        train_team_1_list.append(0.5)
        train_team_2_list.append(0.5)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


def train_attr6():
    # Grabs passing first downs
    if float(train_stats[16]) > float(train_stats[17]):
        train_team_1_list.append(1)
        train_team_2_list.append(0)
    elif float(train_stats[16]) == float(train_stats[17]):
        train_team_1_list.append(0.5)
        train_team_2_list.append(0.5)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


def train_attr7():
    # Grabs rushing first downs
    if float(train_stats[19]) > float(train_stats[20]):
        train_team_1_list.append(1)
        train_team_2_list.append(0)
    elif float(train_stats[19]) == float(train_stats[20]):
        train_team_1_list.append(0.5)
        train_team_2_list.append(0.5)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


def train_attr8():
    # Grabs total yards
    if float(train_stats[34]) > float(train_stats[35]):
        train_team_1_list.append(1)
        train_team_2_list.append(0)
    elif float(train_stats[34]) == float(train_stats[35]):
        train_team_1_list.append(0.5)
        train_team_2_list.append(0.5)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


def train_attr9():
    # Grabs yards per play
    if float(train_stats[40]) > float(train_stats[41]):
        train_team_1_list.append(1)
        train_team_2_list.append(0)
    elif float(train_stats[40]) == float(train_stats[41]):
        train_team_1_list.append(0.5)
        train_team_2_list.append(0.5)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


def train_attr10():
    # Grabs passing yards
    if float(train_stats[43]) > float(train_stats[44]):
        train_team_1_list.append(1)
        train_team_2_list.append(0)
    elif float(train_stats[43]) == float(train_stats[44]):
        train_team_1_list.append(0.5)
        train_team_2_list.append(0.5)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


def train_attr11():
    # grabs yards per pass
    if float(train_stats[49]) > float(train_stats[50]):
        train_team_1_list.append(1)
        train_team_2_list.append(0)
    elif float(train_stats[49]) == float(train_stats[50]):
        train_team_1_list.append(0.5)
        train_team_2_list.append(0.5)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


def train_attr12():
    # Grabs rushing yards
    if float(train_stats[58]) > float(train_stats[59]):
        train_team_1_list.append(1)
        train_team_2_list.append(0)
    elif float(train_stats[58]) == float(train_stats[59]):
        train_team_1_list.append(0.5)
        train_team_2_list.append(0.5)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


def train_attr13():
    # Grabs yards per rush
    if float(train_stats[64]) > float(train_stats[65]):
        train_team_1_list.append(1)
        train_team_2_list.append(0)
    elif float(train_stats[64]) == float(train_stats[65]):
        train_team_1_list.append(0.5)
        train_team_2_list.append(0.5)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


def train_attr14():
    # Grabs turnovers
    if float(train_stats[73]) > float(train_stats[74]):
        train_team_1_list.append(1)
        train_team_2_list.append(0)
    elif float(train_stats[73]) == float(train_stats[74]):
        train_team_1_list.append(0.5)
        train_team_2_list.append(0.5)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


def train_attr15():
    # Grabs possession minutes
    x = train_stats[85].split(":")
    y = train_stats[86].split(":")
    if float(x[0]) > float(y[0]):
        train_team_1_list.append(1)
        train_team_2_list.append(0)
    elif float(x[0]) == float(y[0]):
        train_team_1_list.append(0.5)
        train_team_2_list.append(0.5)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


def run_training_attrs():
    train_attr1()
    train_attr2()
    train_attr3()
    train_attr4()
    train_attr5()
    train_attr6()
    train_attr7()
    train_attr8()
    train_attr9()
    train_attr10()
    train_attr11()
    train_attr12()
    train_attr13()
    train_attr14()
    train_attr15()
    if winning_team() == 1:
        train_team_1_list.append(1)
        train_team_2_list.append(0)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


# PROBABILITY OF OUTCOME
def prob_of_win():
    return 0.5


def prob_of_lose():
    return 0.5

def bulk():
    #teamname = "MASTER"
    team = 'trainingdata1.csv'

    list = main.masterlist()
    createTrainingCSV(team)

    for item in list:

        html = requests.get(item).text
        soup = BeautifulSoup(html, 'html5lib')
        # GRAB ALL STAT INFO
        for td_tag in soup.find_all('td'):
            each_stat = td_tag.text
            train_stats.append(each_stat)
            stat = [x.replace('\t', '').replace('\n', '') for x in train_stats]
        print(stat)
        yearstatsForTeam1WIN()
        #yearstatsForTeam2WIN()

        appendCSV(team)
        del train_stats[:]
        del train_team_1_list[:]
        del train_team_2_list[:]
        del stat[:]

    team2 = 'trainingdata2.csv'

    list = main.masterlist()
    createTrainingCSV(team2)

    for item in list:

        html = requests.get(item).text
        soup = BeautifulSoup(html, 'html5lib')
        # GRAB ALL STAT INFO
        for td_tag in soup.find_all('td'):
            each_stat = td_tag.text
            train_stats.append(each_stat)
            stat = [x.replace('\t', '').replace('\n', '') for x in train_stats]
        print(stat)
        #yearstatsForTeam1WIN()
        yearstatsForTeam2WIN()

        appendCSV(team2)
        del train_stats[:]
        del train_team_1_list[:]
        del train_team_2_list[:]
        del stat[:]
bulk()