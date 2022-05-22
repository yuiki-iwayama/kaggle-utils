import matplotlib.pyplot as plt
from kagutils import eda


def test_matplotlib_rcparams():
    assert plt.rcParams["axes.titlecolor"] == "black"
    assert plt.rcParams["text.color"] == "black"
    assert plt.rcParams["xtick.color"] == "black"
    assert plt.rcParams["ytick.color"] == "black"