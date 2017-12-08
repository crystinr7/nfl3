import grabAttributes
import grabTrainingAttributes
import analyzeAndTrain
import train
import test
import printFullDataSet
import featureSelection

def startwithoutdataset():
    #teamname1()
    # MAYBE SWITCH the order

    grabTrainingAttributes.bulk()
    grabAttributes.bulk()
    #teamname2()
    #grabAttributes.bulk()
    analyzeAndTrain.bulk()
    train.bulk()
    print("BEFORE FEATURE SELECTION: ")
    test.bulk()
    printFullDataSet.bulk()

    featureSelection.bulk2()

startwithoutdataset()
