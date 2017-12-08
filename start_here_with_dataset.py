import grabAttributes

import analyzeAndTrain

import test
import featureSelection


def startwithoutdataset():

    grabAttributes.bulk()
    analyzeAndTrain.bulk()

    print("NAIVE BAYES: ")
    test.bulk()
    print("WITH FEATURE SELECTION: ")
    featureSelection.bulk2()

startwithoutdataset()
