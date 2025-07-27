from datasets import load_dataset
from sklearn.model_selection import train_test_split
import numpy as np
import json as jsonlib

ds = load_dataset("scikit-learn/iris", split="train")

print(ds)
print(ds.features)

print(ds[0])

X_data = []
for row in ds:
    tmp = {
        "Id": row["Id"],
        "SepalLengthCm": row["SepalLengthCm"],
        "SepalWidthCm": row["SepalWidthCm"],
        "PetalLengthCm": row["PetalLengthCm"],
        "PetalWidthCm": row["PetalWidthCm"],
    }
    X_data.append(tmp)

y_data = [row["Species"] for row in ds]

X_data = np.array(X_data)
y_data = np.array(y_data)

X_train, X_test, y_train, y_test = train_test_split(
    X_data, y_data, test_size=0.2, random_state=42
)

print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

with open("data/iris_X_train.jsonl", "w") as f:
    for row in X_train:
        f.write(jsonlib.dumps(row) + "\n")

with open("data/iris_X_test.jsonl", "w") as f:
    for row in X_test:
        f.write(jsonlib.dumps(row) + "\n")

with open("data/iris_y_train.jsonl", "w") as f:
    for row in y_train:
        f.write(jsonlib.dumps(row) + "\n")

with open("data/iris_y_test.jsonl", "w") as f:
    for row in y_test:
        f.write(jsonlib.dumps(row) + "\n")
