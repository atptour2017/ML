from svmMLiA_test import *

d,l=loadDataSet('testSet.txt')
c=0.6
toler=0.001
maxIter=40

smoSimple(d,l,c,toler,maxIter)

