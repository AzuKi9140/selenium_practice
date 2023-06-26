import datetime
import os


def create_directory_if_not_exists(date: datetime) -> str:
    """保存先のディレクトリを作成する

    Args:
        date (datetime): 現在の日付

    Returns:
        full_path (str): 保存先のディレクトリのパス
    """

    # 日付からディレクトリ名を作成
    directory_name = date.strftime("%Y-%m-%d")
    # '/data' 以下に日付のディレクトリを作成
    full_path = os.path.join("data", directory_name)
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    return full_path
