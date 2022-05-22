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
        self.save_path (str):
            path to the directory containing the all competition data files

    Methods:
        competition_download_files():
            Download and unzip the zip containing all competition data files.
        read_csv():
            Load the csv file in the directory where you saved the dataset into DataFrame.
        competition_submit():
            Convert the pd.DataFrame to a csv file and submit it to the competition.
    """

    def __init__(self, competition_id: str, api_client: None=None):
        """
        Constructs all the attributes for the Competition class.

        Parameters:
            self.competition_id: str
                competition_id of the competition
            self.api_client: None default None
                api_client for kaggle.com

        Raises:
            VauleError: When a competition_id that is not currently held is specified as an argument.
        """
        super().__init__(api_client=api_client)
        self.authenticate()
        if competition_id not in list(map(str, self.competitions_list(search=competition_id))):
            raise ValueError("Non-existent competition_id.")
        self._competition_id = competition_id

    @property
    def competition_id(self):
        return self._competition_id

    @property
    def save_path(self):
        return self._save_path

    def competition_download_files(self, path: str=None, force: bool=False, quiet: bool=True, save_name: str="data") -> None:
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
        file_name = self._competition_id + ".zip"
        if path is None:
            file_path = file_name
            self._save_path = save_name
        else:
            file_path = os.path.join(path, file_name)
            self._save_path = os.path.join(path, save_name)

        if os.path.isdir(self._save_path) and force == False:
            return None

        super().competition_download_files(self._competition_id, path, force, quiet)
        shutil.unpack_archive(file_path, self._save_path)
        os.remove(file_path)

    def read_csv(self, name: str, **kwargs) -> pd.core.frame.DataFrame:
        """Wrapper function for pd.read_csv()

        Load the csv file in the directory where you saved the dataset into pandas.DataFrame.

        Parameters:
            name (str):
                filename without extension

        Returns
            pandas.core.frame.DataFrame:
                pandas.DataFrame read from csv file in the directory where you saved the dataset
        """
        file_path = os.path.join(self._save_path, name + ".csv")

        print(f"Load: {file_path}")
        return pd.read_csv(file_path, **kwargs)

    def competition_submit(self, df: pd.core.frame.DataFrame, message: str, file_name: str, path: str=None, quiet: bool=False) -> None:
        """Submit to competition

        Convert the pandas.DataFrame to a csv file and submit it to the competition.

        Parameters:
            df (pd.core.frame.DataFrame):
                pandas.DataFrame containing meta data to be submitted
            message (str):
                the submission description
            file_name: str
                the competition metadata file, extension is always csv
            path (str) default `None`
                file path to the competition metadata file
            quiet (bool): default `False`
                suppress verbose output

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
            csv_file_path = file_name + ".csv"
        else:
            os.makedirs(path, exist_ok=True)
            csv_file_path = os.path.join(path, file_name + ".csv")

        df.to_csv(csv_file_path, index=False, sep=",")
        super().competition_submit(csv_file_path, message, self._competition_id, quiet)


if __name__ == "__main__":
    spaceship_titanic = Competition("spaceship-titanic")
    print(spaceship_titanic.competitions_list())