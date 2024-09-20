"""Class to prepare data and train various machine learning models, 
including logistic regression, decision tree, and random forest classifiers.

Usage :
    trainer = ModelTrainer(data)
    trainer.prepare_data()
    trainer.train_logistic_regression()
    trainer.train_decision_tree()
    trainer.train_random_forest()
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


class ModelTrainer:
    def __init__(self, data):
        self.data = data
        self.X = None
        self.y = None

    def prepare_data(self):
        self.y = self.data["status"]
        self.X = self.data.drop(columns=["status"])

        scaler = StandardScaler()
        self.X_scaled = scaler.fit_transform(self.X)
        self.X_train, self.X_val, self.y_train, self.y_val = train_test_split(
            self.X_scaled, self.y, test_size=0.3, random_state=42
        )

    def train_logistic_regression(self):
        logistic_model = LogisticRegression()
        logistic_model.fit(self.X_train, self.y_train)

        y_pred = logistic_model.predict(self.X_val)
        accuracy = accuracy_score(self.y_val, y_pred)
        f1 = f1_score(self.y_val, y_pred, average="weighted")
        print(f"Logistic Regression - Accuracy: {accuracy}, F1-score: {f1}")

        importance = (
            pd.Series(logistic_model.coef_[0], index=self.X.columns)
            .abs()
            .sort_values(ascending=False)
        )
        print("Logistic Regression - Feature Importance:\n", importance)

    def train_decision_tree(self):
        tree_model = DecisionTreeClassifier()
        tree_model.fit(self.X_train, self.y_train)

        y_pred = tree_model.predict(self.X_val)
        accuracy = accuracy_score(self.y_val, y_pred)
        f1 = f1_score(self.y_val, y_pred, average="weighted")
        print(f"Decision Tree - Accuracy: {accuracy}, F1-score: {f1}")

        importance = (
            pd.Series(tree_model.feature_importances_, index=self.X.columns)
            .sort_values(ascending=False)
        )
        print("Decision Tree - Feature Importance:\n", importance)

    def train_random_forest(self):
        rf_model = RandomForestClassifier()
        rf_model.fit(self.X_train, self.y_train)

        y_pred = rf_model.predict(self.X_val)
        accuracy = accuracy_score(self.y_val, y_pred)
        f1 = f1_score(self.y_val, y_pred, average="weighted")
        print(f"Decision Tree - Accuracy: {accuracy}, F1-score: {f1}")

        importance = (
            pd.Series(rf_model.feature_importances_, index=self.X.columns)
            .sort_values(ascending=False)
        )
        print("Random Forest - Feature Importance:\n", importance)
