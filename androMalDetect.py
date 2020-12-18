import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pickle
from consts import evalTries
import time

from genFeatureSets import featureSet

with open('featureSet', 'rb') as f:
    fs = pickle.load(f)

start = time.time()
accuracy = []
for tries in range(evalTries):
    X_train, X_test, y_train, y_test = train_test_split(fs.data, fs.ans, test_size = 0.2)

    sc = StandardScaler()
    sc.fit(X_train)

    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)


    svm_model = SVC(kernel='rbf')

    svm_model.fit(X_train_std, y_train)
    y_pred = svm_model.predict(X_test_std) # 테스트

    accuracy.append(np.mean(y_pred == y_test))

print("evalTries: {}".format(evalTries))
print("time :", time.time() - start)
print("mean accuracy: {}".format(np.mean(accuracy)))
print("분산(Variance): {}".format(np.var(accuracy)))
print("표준편차(standard deviation): {}".format(np.std(accuracy)))

