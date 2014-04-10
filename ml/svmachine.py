# svmachine
# requires build & install of PyML (pyml.sourceforge.net)

import PyML
from PyML import *

datfile = 'google.data'
# CSV organized like so:
# size, time delta, IsDestinationBlocked

data = VectorDataSet(datfile, labelsColumn = -1)
# the -1 means the last column (the Blocked boolean)

print data

s = SVM()

print s

s.train(data)

#r = s.cv(data, numFolds=5)
#s.save(filename)
#new_svm = SVM() ;; new_svm.load(filename, data) ;; results = new_svm.test(test_data)

print s
