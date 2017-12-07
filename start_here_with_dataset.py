import grabAttributes

import analyzeAndTrain

import test
import featureSelection


def startwithoutdataset():
    #teamname1()
    # MAYBE SWITCH the order


    grabAttributes.bulk()
    #teamname2()
    #grabAttributes.bulk()
    analyzeAndTrain.bulk()

    print("BEFORE FEATURE SELECTION: ")
    test.bulk()
    #printFullDataSet.bulk()
    print("AFTER FEATURE SELECTION: ")
    featureSelection.bulk2()

startwithoutdataset()
