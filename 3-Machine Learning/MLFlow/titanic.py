

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import mlflow
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectKBest
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns

# Loading data and prepping for training
df = pd.read_csv('titanic_modified.csv')

X = df.drop(columns='Survived').values
y = df[['Survived']].values.ravel()

X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    random_state=42)

grid_random_forest = {"n_estimators": [120],
                     "max_depth": [3],
                     "max_features": [4]
                     }

svm_param = {
            'selectkbest__k': [1,2,3],
            'svm__C': [0.8, 0.9]
            }

rand_forest = RandomForestClassifier()

svm = Pipeline([("scaler",StandardScaler()),
                ("selectkbest",SelectKBest()),
                ("svm",SVC())
               ])

# Almaceno en una lista de tuplas los modelos (nombre que le pongo, el modelo, hiperparametros)
models = [('rand_forest', rand_forest, grid_random_forest),
          ('svm', svm, svm_param)]

# Declaro en un diccionario los pipelines e hiperparametros
models_gridsearch = {}

def write_mlflow(model, name, Y, Y_pred):
    with mlflow.start_run(run_name=name):
        mlflow.set_experiment('NLP Experiments')

        mlflow.log_metric('accuracy', accuracy_score(Y, Y_pred))
        mlflow.log_metric('precision', precision_score(Y, Y_pred))
        mlflow.log_metric('recall', recall_score(Y, Y_pred))
        mlflow.log_metric('f1-score', f1_score(Y, Y_pred))

        # ARTIFACTS
        conf_figure = sns.heatmap(confusion_matrix(Y, Y_pred), annot=True)
        fig = conf_figure.get_figure()
        fig.savefig('conf_matrix.png')

        mlflow.log_artifact('conf_matrix.png')

        # MODEL
        mlflow.sklearn.log_model(model, name)

        # PARAMETERS
        if type(model).__name__ == 'RandomForestClassifier':
            mlflow.log_param('max_depth', model.max_depth)

        elif type(model).__name__ == 'Pipeline':
            mlflow.log_param('kernel', model['svm'].kernel)

for i in models:
    grid = GridSearchCV(i[1],
                        i[2],
                        cv = 5,
                        scoring = 'accuracy')

    grid.fit(X_train, y_train)

    predictions = grid.best_estimator_.predict(X_test)
    write_mlflow(grid.best_estimator_, i[0], y_test, predictions)