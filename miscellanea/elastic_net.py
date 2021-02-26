from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split
from egeaML.egeaML import DataIngestion

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

raw_data = DataIngestion(
    df='/content/drive/MyDrive/Machine Learning/Bocconi - Feb 2021/Lecture_02/boston.csv',
    col_target='MEDV'
    )

df = raw_data.load_data()

X = raw_data.features()
y = raw_data.target()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


steps = [
         ('scaler', StandardScaler()),
         ('elasticnet', ElasticNet())
         ]

pipeline = Pipeline(steps)
parameters = {
    'elasticnet__l1_ratio': np.linspace(0, 1, 30), # eta
    }
elastic_cv = GridSearchCV(pipeline, param_grid=parameters)
elastic_cv.fit(X_train, y_train)
r2 = elastic_cv.score(X_test, y_test)

print(f"Tuned ElasticNet Alpha: {elastic_cv.best_params_}")
print(f"Tuned ElasticNet R squared: {r2}")
