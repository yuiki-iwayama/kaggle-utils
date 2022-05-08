from kaggle.api.kaggle_api_extended import KaggleApi
import os
import pandas as pd
import shutil


class Competition(KaggleApi):

    def __init__(self, competition_name: str, api_client=None):
        super().__init__(api_client=api_client)
        self.competition_name = competition_name

    @classmethod
    def api_authenticate(cls, competition_name: str) -> Competition:
        competition = cls(competition_name)
        competition.authenticate()
        return competition

    def competition_download_files(self, path: str=None, force: Bool=False, quiet: Bool=True, save_name: str="datas") -> None:
        super().competition_download_files(self.competition_name, path, force, quiet)

        file_name = self.competition_name + ".zip"
        if path is None:
            file_path = file_name
            save_path = save_name
        else:
            file_path = path + file_name
            save_path = path + save_name
        shutil.unpack_archive(file_path, save_path)
        os.remove(file_path)

        return None

    def competition_submit(self, df: pd.DataFrame, csv_file_path: str, message: str, quiet: Bool=False) -> None:
        df.to_csv(csv_file_path, index=False, sep=",")
        super().competition_submit(csv_file_path, message, self.competition_id, quiet)

        return None