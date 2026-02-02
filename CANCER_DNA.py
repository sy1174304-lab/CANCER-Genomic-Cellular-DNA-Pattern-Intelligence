import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Genome data load karein
genome_data = pd.read_csv('genome_data.csv')

# Data preprocess karein
genome_data = genome_data.dropna() # missing values ko remove karein
genome_data = genome_data.apply(lambda x: x - x.mean()) # data ko normalize karein

# Feature extraction karein
features = genome_data.drop(['cancer_status'], axis=1) # features ko select karein
target = genome_data['cancer_status'] # target variable ko select karein

# Machine learning model train karein
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Model evaluation karein
y_pred = model.predict(X_test)
print('Accuracy:', accuracy_score(y_test, y_pred))
print('Classification Report:')
print(classification_report(y_test, y_pred))
print('Confusion Matrix:')
print(confusion_matrix(y_test, y_pred))


