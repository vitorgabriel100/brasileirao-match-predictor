import pandas as pd


def definir_resultado(row):
    if row["mandante_Placar"] > row["visitante_Placar"]:
        return "casa"
    elif row["mandante_Placar"] < row["visitante_Placar"]:
        return "fora"
    return "empate"


def main():
    df = pd.read_csv("data/campeonato-brasileiro-full.csv")

    df["resultado"] = df.apply(definir_resultado, axis=1)

    df = df[["mandante", "visitante", "resultado"]]

    df.to_csv("data/jogos_tratados.csv", index=False)

    print("Arquivo tratado salvo em data/jogos_tratados.csv")


if __name__ == "__main__":
    main()