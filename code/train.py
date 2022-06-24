# Import packages
from distutils.log import Log
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import pandas as pd
import joblib
import gzip
import feature_engine
import river

# load the dataset
data = pd.read_csv("./data/wdbc.csv",header=None)

# preprocess dataset
data = data.set_index([0])

data[1] = data[1].replace(['B', 'M'], [0,1])
print(data[1])
# create x,y 
y = data.pop(1)
x = data
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

# create the ensemble models
estimators = []
estimators.append(('logistic', LogisticRegression()))
estimators.append(('cart', DecisionTreeClassifier()))
estimators.append(('svm', SVC()))

# create the ensemble model
ensemble = VotingClassifier(estimators)

# make preprocess pipeline
pipe = Pipeline([
    ('imputer', SimpleImputer()),
    ('scaler', MinMaxScaler()),
    ('model', ensemble)
])

# Train the model
pipe.fit(x_train, y_train)

# test accuracy
print("Accuracy: %s" % str(pipe.score(x_test, y_test)))

# plot confusion matrix
print("Confusion matrix: \n", ConfusionMatrixDisplay.from_estimator(pipe, x_test, y_test))
plt.show()

# export model
joblib.dump(pipe, gzip.open('./model/model_binary.dat.gz', 'wb'))