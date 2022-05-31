import matplotlib.pyplot as plt


def stacked_bar_plot(df, ax=None, orient="v", colors=None, title=None, text_num=0, **kwargs):

    if ax is None:
        ax = plt.subplot(1, 1, 1)
    if orient == "v":
        __stacked_bar(df, ax, colors, text_num)
    elif orient == "h":
        __stacked_barh(df, ax, colors, text_num)
    else:
        raise ValueError("Incorrect value, specify `h` for horizontal bars and `v` for vertical bars.")

    ax.legend(labels=df.index, **kwargs)
    ax.set_title(title)


def __stacked_bar(df, ax, colors, text_num):
    df.T.plot.bar(ax=ax, stacked=True, color=colors)
    for i_index in range(df.shape[0]):
        for j_index in range(df.shape[1]):
            if df.iloc[i_index, j_index] > text_num:
                ax.text(
                    x=j_index,
                    y=df.iloc[:i_index, j_index].sum() + (df.iloc[i_index, j_index] / 2),
                    s=df.iloc[i_index, j_index],
                    ha="center",
                    va="center"
                )
    ax.set_xticklabels(labels=df.columns, rotation=0)


def __stacked_barh(df, ax, colors, text_num):
    df.T.plot.barh(ax=ax, stacked=True, color=colors)
    for i_index in range(df.shape[0]):
        for j_index in range(df.shape[1]):
            if df.iloc[i_index, j_index] > text_num:
                ax.text(
                    x=df.iloc[:i_index, j_index].sum() + (df.iloc[i_index, j_index] / 2),
                    y=j_index,
                    s=df.iloc[i_index, j_index],
                    ha="center",
                    va="center"
                )