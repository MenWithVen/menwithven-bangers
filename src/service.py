from enum import Enum

from src.utils import parse_json_from_file, write_json_to_file


def update_json_bollocks(file_path: str,
                         key: str,
                         args: dict):
    data = parse_json_from_file(file_path=file_path)
    data[key].append(args)
    write_json_to_file(file_path=file_path,
                       content=data)
