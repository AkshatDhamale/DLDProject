import random
import pandas as pd 
import numpy as np
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

dataset = pd.read_csv("training_data.csv")
testing_data = pd.read_csv("testing_data_final.csv")

print(dataset.groupby('eligibility').size())

pyplot.rcParams.update({"font.size":80})
pyplot.figure(figsize=(50,50))
dataset.plot(kind='box',subplots=True,layout=(6,2),sharex=False,sharey=False, figsize=(50,50))


scatter_matrix(dataset,figsize=(50,50))
pyplot.show()

array = dataset.values
testarray = testing_data.values
X_train = np.concatenate((array[:,3:7],array[:,8:9],array[:,10:11],array[:,12:13],array[:,14:15],
                          array[:,16:17],array[:,18:19]),axis=1)
Y_train = array[:,20]
X_validation = np.concatenate((testarray[:,3:7],testarray[:,8:9],testarray[:,10:11],
                               testarray[:,12:13],testarray[:,14:15],testarray[:,16:17],
                               testarray[:,18:19]),axis=1)
Y_validation = testarray[:,20]

models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))

# evaluate each model in turn

results = []
names = []
for name, model in models:
	kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
	cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
	results.append(cv_results)
	names.append(name)
	print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))
    
bp = pyplot.boxplot(results[:6:2], labels=names[:6:2],positions=[1,3,5], patch_artist=True, whiskerprops = dict(linestyle='--'
                           , linewidth=2))
for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
    pyplot.setp(bp[element], color='red')

    for patch in bp['boxes']:
        patch.set(facecolor='orange') 

bp2 = pyplot.boxplot(results[1:6:2], labels=names[1:6:2],positions=[2,4,6],patch_artist=True, whiskerprops = dict(linestyle='--'
                           , linewidth=2))
for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
    pyplot.setp(bp2[element], color='purple')

    for patch in bp2['boxes']:
        patch.set(facecolor='violet') 

pyplot.title('Algorithm Comparison')   
pyplot.grid(True)
pyplot.savefig('demo3.png', transparent=True)

model = LinearDiscriminantAnalysis()
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)

print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))
