from linear_svm_clf import LinearSVMClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import numpy as np
import os, sys
import matplotlib.pyplot as plt
import seaborn as sns


def plot(log, dir='./log'):
    if not os.path.exists(dir):
        os.makedirs(dir)
    sns.set(style='white')
    plt.plot(log['loss'], label='train_loss')
    plt.plot(log['val_loss'], label='test_loss')
    plt.legend(loc='best')
    plt.savefig(os.path.join(dir, sys.argv[0][:-3]))
    print("Figure created !")


if __name__ == '__main__':
    X, y = make_classification(1000)
    for idx, val in enumerate(y):
        if val == 0:
            y[idx] = -1
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

    clf = LinearSVMClassifier(C=1.0, n_in=X_train.shape[1])
    log = clf.fit(X_train, y_train.reshape(-1, 1), n_epoch=100, batch_size=32,
                  validation_data=(X_test, y_test.reshape(-1, 1)))
    y_pred = clf.predict(X_test)
    print("linear svm (tensorflow):", np.equal(y_pred.ravel(), y_test[:len(y_pred)]).astype(float).mean())
    clf.close()

    plot(log)

    clf = SVC(kernel='linear')
    y_pred = clf.fit(X_train, y_train).predict(X_test)
    print("linear svm (sklearn):", np.equal(y_pred, y_test).astype(float).mean())