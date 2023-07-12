import pandas as pd


def main():
    df = pd.read_csv("pois_all_info.csv", sep='\t')
    print(df)
    ny_muns = pd.read_csv("ny_municipality_pois_id.csv", names=["@id"], nrows=100).values.tolist()
    df = df[df[df.columns[0]].isin(ny_muns)]
    print(df)


if __name__ == '__main__':
    main()
