from kagutils import Competition
import os
import pandas as pd
import pytest
import shutil


def test_create_competition_instance():
    compe = Competition("titanic")
    with pytest.raises(ValueError):
        Competition("test")
    assert compe.competition_id == "titanic"


def test_non_param_download_files():
    compe = Competition("titanic")
    compe.competition_download_files()
    assert os.path.isdir("data")
    assert compe.save_path == "data"
    shutil.rmtree("data")


def test_set_path_download_files():
    compe = Competition("titanic")
    compe.competition_download_files(path="/work/data", save_name="test")
    assert os.path.isdir("/work/data/test")
    assert compe.save_path == "/work/data/test"
    shutil.rmtree("/work/data")


def test_read_csv():
    compe = Competition("titanic")
    compe.competition_download_files()
    df = compe.read_csv("gender_submission")
    assert type(df) == type(pd.DataFrame())


def test_non_path_submit():
    compe = Competition("titanic")
    compe.competition_download_files()
    df = compe.read_csv("gender_submission")
    compe.competition_submit(df, message="test", file_name="test_sub")
    assert os.path.isfile("test_sub.csv")
    shutil.rmtree("data")
    os.remove("test_sub.csv")


def test_path_submit():
    compe = Competition("titanic")
    compe.competition_download_files()
    df = compe.read_csv("gender_submission")
    compe.competition_submit(df, message="test", file_name="test_sub", path="/work/submission")
    assert os.path.isfile("/work/submission/test_sub.csv")
    shutil.rmtree("data")
    shutil.rmtree("/work/submission")