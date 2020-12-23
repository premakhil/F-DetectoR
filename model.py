# from google.colab import drive
# drive.mount('/content/gdrive')

import pandas as pd

import numpy as np
import scipy.optimize as opt
from sklearn import preprocessing
# %matplotlib inline 
import matplotlib.pyplot as plt
import pylab as pl


import pickle #Modifications for flask

text = open("./paysim.csv", "r")

#join() method combines all contents of
# csvfile.csv and formed as a string
text = ''.join([i for i in text])

# search and replace the contents
text = text.replace("PAYMENT", "1")
text = text.replace("TRANSFER", "2")
text = text.replace("CASH_IN", "3")
text = text.replace("CASH_OUT", "4")
text = text.replace("DEBIT", "5")
# output.csv is the output file opened in write mode
x = open("./output.csv", "w")

# all the replaced text is written in the output.csv file
x.writelines(text)
x.close()

churn_df = pd.read_csv('./output.csv')

X = np.asarray(churn_df[['step', 'type', 'amount', 'oldbalanceOrg', 'newbalanceOrig',
        'oldbalanceDest', 'newbalanceDest']])

y = np.asarray(churn_df['isFraud'])

from sklearn import preprocessing
X = preprocessing.StandardScaler().fit(X).transform(X)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
LR = LogisticRegression(C=0.01, solver='liblinear').fit(X_train, y_train)

yhat = LR.predict(X_test)

yhat_prob = LR.predict_proba(X_test)

# from sklearn.metrics import jaccard_similarity_score
# jaccard_similarity_score(y_test, yhat)  #it is an output

# step=float(input())
# transtype=float(input())
# amount=float(input())
# nameorig=str(input())
# oldbalanceOrg=float(input())
# newbalanceOrig=float(input())
# namedest=str(input())
# oldbalanceDest=float(input())
# newbalanceDest=float(input())

# Z = [[step, transtype, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest]]


from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
LR = LogisticRegression(C=0.01, solver='liblinear').fit(X_train, y_train)

pickle.dump(LR, open('model.pkl', 'wb'))            #Flask modifications

model = pickle.load(open('model.pkl', 'rb'))


yhat = LR.predict(Z)

