import pandas as pd


def create_target_piovt(df, column, target, normalize=False, dropna=False):
    df_label_pivvot = pd.DataFrame()
    for label in df[target].unique():
        if pd.isna(label):
            _df = df[pd.isna(df[target])][column].value_counts(normalize=normalize, dropna=dropna)
        else:
            _df = df[df[target] == label][column].value_counts(normalize=normalize, dropna=dropna)
        df_label_pivvot = pd.concat(
            [
                df_label_pivvot,
                _df
            ],
            axis=1
        )
    return df_label_pivvot.set_axis(df[target].unique(), axis=1)


def create_label_pivot(train, test, label, normalize=False, dropna=False):
    df = pd.concat(
        [
            train[label].value_counts(normalize=normalize, dropna=dropna),
            test[label].value_counts(normalize=normalize, dropna=dropna)
        ],
        axis=1
    )
    return df.set_axis(["Train", "Test"], axis=1)