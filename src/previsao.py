import joblib
import pandas as pd


modelo = joblib.load("models/modelo.pkl")


def prever_resultado(mandante, visitante):
    entrada = pd.DataFrame([{
        "mandante": mandante,
        "visitante": visitante
    }])

    probabilidades = modelo.predict_proba(entrada)[0]
    classes = modelo.classes_

    return {
        classe: prob
        for classe, prob in zip(classes, probabilidades)
    }