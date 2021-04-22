

import mlflow

experiment_id = mlflow.create_experiment('NLP Experiments')
experiment = mlflow.get_experiment(experiment_id)
print('Name:', experiment.name)
print('Experiment Id:', experiment.experiment_id)
print('Location:', experiment.artifact_location)
print('Tags:', experiment.tags)