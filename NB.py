import IPython
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib
import sklearn
from sklearn import cross_validation
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

def split_train_test(X, Y):
    X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(
    X, Y, test_size=0.66, random_state=19)
    return X_train, X_test, Y_train, Y_test
    
def make_xy(df, vectorizer=None):
    text = np.asarray(df.text)
    vectorizer.fit(text)
    X = vectorizer.transform(text)
    X = X.toarray()
    Y = np.where(df['codes.0.first_code'] == 'Affirm', 1, 0).copy()
    return X, Y

def log_likelihood(model, x, y):
    prob = model.predict_log_proba(x)
    #find deny or affirm in the target
    deny = y == 0
    affirm = ~deny
    #the first column of prob indicates the log likelihood of being denials, while the second ... being affirms
    return prob[deny, 0].sum() + prob[affirm, 1].sum()

def naive_bayes(data, min_df, alpha):
    vectorizer = CountVectorizer(min_df= min_df)
    X, Y = make_xy(data, vectorizer)
    X_train, X_test, Y_train, Y_test = split_train_test(X, Y)
    fitted_model = MultinomialNB(alpha = alpha)
    fitted_model.fit(X_train, Y_train)
    print fitted_model.score(X_train, Y_train)
    print fitted_model.score(X_test, Y_test)
