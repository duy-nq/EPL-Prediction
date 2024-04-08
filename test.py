from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

FILENAME = 'training_data.csv'


def map_outcome(outcome):
    if outcome == 'WIN' or outcome == 'DRAW':
        return 'HAVE POINT'
    else:
        return '0 POINT'

def read_data(file: str):
    df = pd.read_csv(file, sep=',')

    df['h_str'] = df['h_str'] + 2

    X = df.drop('result', axis=1)
    y = df['result']

    return X, y

X, y = read_data(FILENAME)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=56, random_state=42)
model_linear = LogisticRegression(multi_class='multinomial', max_iter=1000)
model_svm = SVC(kernel='poly')

# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)

# model_linear.fit(X_train, y_train)
# y_pred_linear = model_linear.predict(X_test)

model_svm.fit(X_train, y_train)
y_pred_svm = model_svm.predict(X_test)

print('MODEL:', accuracy_score(y_test, y_pred_svm))