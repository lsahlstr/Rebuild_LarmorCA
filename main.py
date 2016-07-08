#!/Users/lsahlstr/anaconda/bin/python

from organize_data import OrganizeData
from sklearn.ensemble.forest import RandomForestRegressor
from sklearn.cross_validation import cross_val_score
import sys
#import my_plotting
import numpy as np

if __name__ == "__main__":
    
    nucleus = 'N' # make command line option; supported nuclei are ['H','N','CA','HA','CB','C']
    X_train,y_train = OrganizeData(nucleus, 'train')        
    X_test, y_test = OrganizeData(nucleus, 'test')
        
    # Set the parameters for the random forest estimator    
    estimator = RandomForestRegressor(n_estimators=50, max_features=2, max_depth=25,
    				min_samples_leaf=5, random_state=0)
    
    # Build the random forest of regression trees from the training set
    estimator = estimator.fit(X_train,y_train)
    
    print estimator.score(X_train,y_train)
    print estimator.score(X_test,y_test)
        
    # Predict regression target for the test set
    predicted = estimator.predict(X_test)
    cc = np.corrcoef(y_test,predicted)
    print cc
    print estimator
    #my_plotting.simple_plot_overlay(y_test,predicted)
    
    # score = cross_val_score(estimator, X_train, y_train)
#     print score 