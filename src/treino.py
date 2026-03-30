import pandas as pd
import joblib

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression


def main():
    df = pd.read_csv("data/jogos_tratados.csv")

    X = df[["mandante", "visitante"]]
    y = df["resultado"]

    preprocessador = ColumnTransformer(
        transformers=[
            (
                "cat",
                OneHotEncoder(handle_unknown="ignore"),
                ["mandante", "visitante"]
            )
        ]
    )

    modelo = Pipeline(steps=[
        ("preprocessamento", preprocessador),
        ("classificador", LogisticRegression(max_iter=1000))
    ])

    modelo.fit(X, y)

    joblib.dump(modelo, "models/modelo.pkl")

    print("Modelo treinado e salvo em models/modelo.pkl")


if __name__ == "__main__":
    main()