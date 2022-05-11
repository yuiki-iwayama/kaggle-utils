from kaggle import KaggleApi
import os
import pandas as pd
import shutil


class Competition(KaggleApi):
    """
    The competition class is the child of the KaggleApi class and represents the Kaggle competition.

    Attributes:
        self.competition_id (str):
            competition_id of the competition
        self.api_client  (None): default `None`
            api_client for kaggle.com
        self.save_path

    Methods:
        competition_download_files():
            Download and unzip the zip containing all competition data files.
        read_csv():
            Load the csv file in the directory where you saved the dataset into DataFrame.
        competition_submit():
            Convert the pd.DataFrame to a csv file and submit it to the competition.
    """

    def __init__(self, competition_id, api_client=None):
        """
        Constructs all the attributes for the Competition class.

        Parameters:
            self.competition_id: str
                competition_id of the competition
            self.api_client: None default None
                api_client for kaggle.com
        """
        super().__init__(api_client=api_client)
        self.competition_id = competition_id
        self.authenticate()

    def competition_download_files(self, path=None, force=False, quiet=True, save_name="data"):
        """Download all competition data files

        Download and unzip the zip containing all competition data files.

        Parameters:
            path: str, default `None`
                a path to the directory containing the all competition data files to
            force: bool, default `False`
                force the download if the file already exists (default False)
            queit: bool, default `True`
                suppress verbose output (default is True)
            save_name:str, default `data`
                a directory name containing the all competition data files

        Returns:
            None

        Examples:
            >>> from kagutils.utils import Competition
            >>> hoge = Competition("hoge")
            >>> hoge.cometition_download_files()
        """
        file_name = self.competition_id + ".zip"
        if path is None:
            file_path = file_name
            self.save_path = save_name
        else:
            file_path = os.path.join(path, file_name)
            self.save_path = os.path.join(path, save_name)

        if os.path.isdir(self.save_path) and force == False:
            return None

        super().competition_download_files(self.competition_id, path, force, quiet)
        shutil.unpack_archive(file_path, save_path)
        os.remove(file_path)

    def read_csv(self, name, **kwargs):
        """Wrapper function for pd.read_csv()

        Load the csv file in the directory where you saved the dataset into pd.DataFrame.

        Parameters:
            name (str):
                filename without extension

        Returns
            pd.DataFrame:
                pd.DataFrame read from csv file in the directory where you saved the dataset
        """
        file_path = os.path.join(self.save_path, name + ".csv")

        print(f"Load: {file_path}")
        return pd.read_csv(file_path, **kwargs)

    def competition_submit(self, df, message, file_name, path=None, quiet=False):
        """Submit to competition

        Convert the pd.DataFrame to a csv file and submit it to the competition.

        Parameters:
            df (pd.DataFrame):
                pd.DataFrame containing meta data to be submitted
            message (str):
                the submission description
            file_name: str
                the competition metadata file, extension is always csv
            path (str) default `None`
                file path to the competition metadata file
            quiet (bool): default `False`
                suppress verbose output (default is False)

        Returns:
            None

        Examples:
            >>> from kagutils.utils import Competition
            >>> import os
            >>> hoge = Competition("hoge")
            >>> os.mkdir("./submission")
            >>> hoge.competition_submit(df, message="first submission", file_name="1st", path="./submission/")
        """
        if path is None:
            file_path = file_name + ".csv"
        else:
            file_path = os.join.path(path, file_name + ".csv")

        df.to_csv(file_path, index=False, sep=",")
        super().competition_submit(csv_file_path, message, self.competition_id, quiet)


if __name__ == "__main__":
    titanic = Competition("titanic")
    print(titanic.competitions_list())