import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectFromModel
from sklearn.decomposition import PCA
from sklearn.model_selection import GridSearchCV
from sklearn.feature_selection import mutual_info_classif
from sklearn.feature_selection import SelectKBest
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt
from sklearn.inspection import permutation_importance
import shap

train_df = pd.read_csv('/content/ML2025Spring-hw2-public/train.csv')
test_df = pd.read_csv('/content/ML2025Spring-hw2-public/test.csv')
submission_df = pd.read_csv('/content/ML2025Spring-hw2-public/sample_submission.csv')

# Drop highly correlated independent variables to prevent multicollinearity
corr_matrix = train_df.corr()
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
to_drop = [column for column in upper.columns if any(abs(value) > 0.7 for value in upper[column].dropna())]
train_df.drop(to_drop, axis=1, inplace=True)

# Use Mutual Information (MI) to assess categorical features
mutual_info = mutual_info_classif(train_df.drop('tested_positive_day3', axis=1), train_df['tested_positive_day3'])
feature_names = train_df.drop('tested_positive_day3', axis=1).columns
feature_names = [x for _, x in sorted(zip(mutual_info, feature_names), reverse=True)]
train_df.drop(feature_names[mutual_info < 0.1], axis=1, inplace=True)
test_df.drop(feature_names[mutual_info < 0.1], axis=1, inplace=True)

# Compute the correlation matrix and select features with a strong correlation to the target
corr_matrix = train_df.corr()
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
to_drop = [column for column in upper.columns if any(abs(value) > 0.7 for value in upper[column].dropna())]
train_df.drop(to_drop, axis=1, inplace=True)
test_df.drop(to_drop, axis=1, inplace=True)

X_train, X_val, y_train, y_val = train_test_split(train_df.drop('tested_positive_day3', axis=1), train_df['tested_positive_day3'], test_size=0.2, random_state=42)

rf = RandomForestClassifier(random_state=42)
param_grid = {'n_estimators': [100, 200, 300, 400, 500], 'max_depth': [5, 10, 15, 20, 25]}
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error')
grid_search.fit(X_train, y_train)
rf = grid_search.best_estimator_

y_pred = rf.predict(X_val)
mse = mean_squared_error(y_val, y_pred)
print(f'MSE: {mse}')

test_pred = rf.predict(test_df)
submission_df['tested_positive_day3'] = test_pred
submission_df.to_csv('/content/submission.csv', index=False)

explainer = shap.TreeExplainer(rf)
shap_values = explainer.shap_values(X_val)
shap.summary_plot(shap_values, X_val, plot_type='bar')