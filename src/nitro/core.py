from rich import print as rprint
import pandas as pd
import importlib
import sklearn
import numpy as np


def run_experiment(config_dict: dict):
    rprint(config_dict)
    assert len(config_dict) == 1, "Only one experiment is supported"
    experiment_name = list(config_dict.keys())[0]
    # load datasets
    X_train = []
    for filepath in config_dict[experiment_name]["datasets"]["X_train"]:
        X_train.append(pd.read_json(filepath, lines=True).to_numpy())
    y_train = []
    for filepath in config_dict[experiment_name]["datasets"]["y_train"]:
        y_train.append(pd.read_json(filepath, lines=True).to_numpy())
    X_test = []
    for filepath in config_dict[experiment_name]["datasets"]["X_test"]:
        X_test.append(pd.read_json(filepath, lines=True).to_numpy())
    y_test = []
    for filepath in config_dict[experiment_name]["datasets"]["y_test"]:
        y_test.append(pd.read_json(filepath, lines=True).to_numpy())

    X_train = np.concatenate(X_train)
    y_train = np.concatenate(y_train)
    X_test = np.concatenate(X_test)
    y_test = np.concatenate(y_test)

    # run preprocessing
    for preprocessing_step in config_dict[experiment_name]["preprocessing"]:
        preprocessing_step = preprocessing_step.split(".")
        module_name = ".".join(preprocessing_step[:-1])
        class_name = preprocessing_step[-1]
        module = importlib.import_module(module_name)
        class_ = getattr(module, class_name)
        scaler = class_()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

    # run classifier
    if (
        config_dict[experiment_name]["classifier"]
        == "local.classifier.null_classifier.NullClassifier"
    ):
        from local.classifier.null_classifier import NullClassifier

        classifier = NullClassifier()
    else:
        classifier_step = config_dict[experiment_name]["classifier"]
        classifier_step = classifier_step.split(".")
        module_name = ".".join(classifier_step[:-1])
        class_name = classifier_step[-1]
        module = importlib.import_module(module_name)
        class_ = getattr(module, class_name)
        classifier = class_()
        classifier.fit(X_train, y_train)

    # run accuracy scorer
    y_pred = classifier.predict(X_test)
    score = sklearn.metrics.accuracy_score(y_test, y_pred)
    rprint(f"Experiment {experiment_name} score: {score}")
    return score
