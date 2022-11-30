import json


def parse_json_from_file(file_path: str) -> dict:
    with open(file=file_path,
              mode="r") as f:
        return json.load(f)


def write_json_to_file(file_path: str,
                       content: dict) -> None:
    with open(file=file_path,
              mode="w") as f:
        json.dump(content, f)
