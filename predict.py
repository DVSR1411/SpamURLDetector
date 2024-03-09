import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,precision_score, recall_score, f1_score
from keras.models import Sequential
from keras.layers import Dense
df = pd.read_csv('phishing.csv')
df = df.drop("Index",axis=1)
X = df.drop("class",axis=1).values
y = df["class"].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = Sequential()
model.add(Dense(128, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=30)
y_pred = model.predict(X_test)
y_pred = (y_pred > 0.5).astype(int)
accuracy = accuracy_score(y_test, y_pred)
precison = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1score = f1_score(y_test, y_pred)
print(f"Accuracy = {accuracy * 100:.2f}%")
print(f"Precision = {precison * 100:.2f}%")
print(f"Recall = {recall * 100:.2f}%")
print(f"F1 Score = {f1score * 100:.2f}%")
model.save('nnmodel.keras')