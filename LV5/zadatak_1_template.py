import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn . metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn . linear_model import LogisticRegression
from sklearn . metrics import accuracy_score, precision_score, recall_score


X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                           random_state=213, n_clusters_per_class=1, class_sep=1)

# train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=5)

# a)
plt.scatter(X_train[:, 0], X_train[:, 1],
            label="trening", cmap="coolwarm", c=y_train)
plt.scatter(X_test[:, 0], X_test[:, 1],
            label="test", cmap="coolwarm", c=y_test)
plt.xlabel("x1")
plt.ylabel("x2")
plt.savefig("zadatak1_slika1")
plt.show()

# b)
LogRegression_model = LogisticRegression()
LogRegression_model . fit(X_train, y_train)

# c)  Pronadite u atributima izgradenog modela parametre modela.
coef = LogRegression_model.coef_[0]
intercept = LogRegression_model.intercept_


def decision_boundary(x1):
    return (-coef[0]*x1 - intercept) / coef[1]


# Prikažite granicu odluke naucenog modela u ravnini ˇ x1 − x2 zajedno s podacima za ucenje
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='coolwarm')
plt.plot(X_train[:, 0], decision_boundary(X_train[:, 0]))
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Logistic Regression Decision Boundary')
plt.show()

# d)Klasifikacija,izracun i prikaz matrice zabune
y_pred = LogRegression_model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print("Matrica zabune: ", cm)  # ispis matrice
disp = ConfusionMatrixDisplay(
    confusion_matrix(y_test, y_pred))  # prikaz matrice
disp.plot()
plt.savefig("zadatak1_slika2")
plt.show()

print(" Tocnost : ", accuracy_score(y_test, y_pred))
print(" Preciznost : ", precision_score(y_test, y_pred))
print(" Odziv: ", recall_score(y_test, y_pred))

# e) Prikažite skup za testiranje u ravnini x1 −x2. Zelenom bojom oznacite dobro klasificirane primjere dok pogrešno klasificirane primjere oznacite crnom bojom.
plt.scatter(X_test[:, 0], X_test[:, 1], label="test", cmap="seismic", c=y_test)
for i in range(len(y_test)):
    if y_test[i] == y_pred[i]:
        plt.scatter(X_test[i, 0], X_test[i, 1], c='g')
    else:
        plt.scatter(X_test[i, 0], X_test[i, 1], c='k')

plt.xlabel("x1")
plt.ylabel("x2")
plt.savefig("zadatak1_slika3")
plt.show()
