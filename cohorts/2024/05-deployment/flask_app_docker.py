import pickle
from typing import Any

import numpy as np
from flask import Flask, Response, jsonify, request
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

print("Loading model...")
app_root: str = __file__.split(sep="/flask_app_docker.py")[0]
print(app_root)

with open(file="model2.bin", mode="rb") as f_in:
    model: LogisticRegression = pickle.load(file=f_in)

with open(file="dv.bin", mode="rb") as f_in:
    dv: DictVectorizer = pickle.load(file=f_in)

app = Flask(import_name="hw")


@app.route(rule="/predict", methods=["POST"])
def predict() -> Response:
    # can't be used in browser, since it sends a GET request
    record: dict[str, Any] = request.get_json()

    X: np.ndarray = dv.transform(X=[record])  # type: ignore
    y_pred: float = float(model.predict_proba(X=X)[0, 1])
    label: bool = bool(y_pred >= 0.5)

    result: dict[str, float | bool] = {"probability": y_pred, "label": label}

    return jsonify(result)


if __name__ == "__main__":
    # run the code in local machine with the debugging mode true and port 9696
    app.run(debug=True, host="0.0.0.0", port=9696)
