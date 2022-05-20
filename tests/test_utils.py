import pytest

from kagutils.utils import Competition
import os
import pandas as pd
import shutil


def test_competition_access():
    compe = Competition("titanic")
    assert compe.competition_id == "titanic"
    compe.competition_download_files(path="/work/data", save_name="test")
    assert os.path.isdir("/work/data/test")
    assert compe.save_path == "/work/data/test"

    df = compe.read_csv("gender_submission")
    assert type(df) == type(pd.DataFrame())
    os.mkdir("./submission")
    compe.competition_submit(df, message="test", file_name="test_sub", path="/work/submission")

    shutil.rmtree("/work/data")
    shutil.rmtree("/work/submission")