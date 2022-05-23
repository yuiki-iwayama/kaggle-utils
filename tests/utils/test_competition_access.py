from kagutils import Competition
import os
import pandas as pd
import pytest
import shutil


def test_create_competition_instance():
    with pytest.raises(ValueError):
        Competition("test")
    compe = Competition("spaceship-titanic")
    assert compe.competition_id == "spaceship-titanic"


@pytest.fixture()
def competition_titanic():
    competition_titanic = Competition("titanic")
    yield competition_titanic
    shutil.rmtree(competition_titanic.save_path)


def test_non_param_download_files(competition_titanic):
    competition_titanic.competition_download_files()
    assert os.path.isdir("data")
    assert competition_titanic.save_path == "data"


def test_set_path_download_files(competition_titanic):
    competition_titanic.competition_download_files(path="/work/data", save_name="test")
    assert os.path.isdir("/work/data/test")
    assert competition_titanic.save_path == "/work/data/test"


def test_read_csv(competition_titanic):
    competition_titanic.competition_download_files()
    df = competition_titanic.read_csv("gender_submission")
    assert type(df) == type(pd.DataFrame())


def test_non_path_submit(competition_titanic):
    competition_titanic.competition_download_files()
    df = competition_titanic.read_csv("gender_submission")
    competition_titanic.competition_submit(df, message="test", file_name="test_sub")
    assert os.path.isfile("test_sub.csv")
    os.remove("test_sub.csv")


def test_path_submit(competition_titanic):
    competition_titanic.competition_download_files()
    df = competition_titanic.read_csv("gender_submission")
    competition_titanic.competition_submit(df, message="test", file_name="test_sub", path="/work/submission")
    assert os.path.isfile("/work/submission/test_sub.csv")
    shutil.rmtree("/work/submission")