#!/Users/lsahlstr/anaconda/bin/python

from organize_data import OrganizeData
from sklearn import preprocessing
from sklearn.ensemble.forest import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.cross_validation import cross_val_score
import sys
#import my_plotting
import pickle
import numpy as np

if __name__ == "__main__":
    
    nucleus = 'N' # make command line option; supported nuclei are ['H','N','CA','HA','CB','C']
    
    # Generate training and test set
    X_train,y_train = OrganizeData(nucleus, 'train')
    X_test, y_test = OrganizeData(nucleus, 'test')
    
    # Feature scaling
    X_train_scaled = preprocessing.scale(X_train)
    X_test_scaled = preprocessing.scale(X_test)
            
    # Set the parameters for the random forest estimator    
    estimator = RandomForestRegressor(n_estimators=100, max_features=16, max_depth=25,
                    min_samples_split=5, min_samples_leaf=5, random_state=0)
        
    # Build the random forest of regression trees from the training set
    estimator = estimator.fit(X_train_scaled,y_train)
    print estimator
        
    # Predict regression target for the training set
    predicted = estimator.predict(X_train_scaled)
    mae = mean_absolute_error(y_train,predicted)
    print mae
    cc = np.corrcoef(y_train,predicted)
    print cc
    #my_plotting.simple_plot_overlay(y_train,predicted)
    # Save data arrays with pickle
    output = open('cs_pred_train.pkl','w')
    pickle.dump(predicted, output)
    output.close()
    output = open('cs_targ_train.pkl','w')
    pickle.dump(y_train, output)
    output.close()
    
    # Predict regression targe for the test set
    predicted = estimator.predict(X_test_scaled)
    mae = mean_absolute_error(y_test,predicted)
    print mae
    cc = np.corrcoef(y_test,predicted)
    print cc
    #my_plotting.simple_plot_overlay(y_test,predicted)  
    # Save data arrays with pickle
    output = open('cs_pred_test.pkl','w')
    pickle.dump(predicted, output)
    output.close()
    output = open('cs_targ_test.pkl','w')
    pickle.dump(y_test, output)
    output.close()
      
    # Scoring
    # score = cross_val_score(estimator, X_train, y_train)
    # print score
    # print estimator.score(X_train_scaled,y_train)
    # print estimator.score(X_test_scaled,y_test)