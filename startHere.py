import main
import grabAttributes
import grabTrainingAttributes
import analyzeAndTrain
import train
import test

def teamname1():
    return "DET"
def teamname2():
    return "PHI"
teamname1()
grabAttributes.bulk()
teamname2()
grabAttributes.bulk()
grabTrainingAttributes.bulk()
analyzeAndTrain.bulk()
train.bulk()
test.bulk()