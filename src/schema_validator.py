from src.service import FILMS_JSON_FILEPATH, TUNES_JSON_FILEPATH, FILMS_CONTENT_KEY, TUNES_CONTENT_KEY, NAME_KEY, \
    LINK_KEY, ON_NETFLIX_KEY, ON_PRIME_KEY, ARTIST_KEY
from src.utils import parse_json_from_file


class ParsingException(Exception):

    def __init__(self, msg: str):
        super(self).__init__(f"error occurred parsing the file\n{msg}")


def validate_fields(data_set: list[dict],
                    fields: list[str],
                    type: str) -> None:
    for data in data_set:
        for field in fields:
            if field not in data:
                raise ParsingException(f"key: {field} was not found in {type}")
            else:
                print(f"key: {field} was found in {type}")


films_content = parse_json_from_file(file_path=FILMS_JSON_FILEPATH)

try:
    films = films_content[FILMS_CONTENT_KEY]
    validate_fields(data_set=films,
                    fields=[
                        NAME_KEY,
                        LINK_KEY,
                        ON_NETFLIX_KEY,
                        ON_PRIME_KEY
                    ],
                    type="film")
except:
    raise ParsingException(f"key: {FILMS_CONTENT_KEY} was not found")

tunes_content = parse_json_from_file(file_path=TUNES_JSON_FILEPATH)

try:
    tunes = tunes_content[TUNES_CONTENT_KEY]
    validate_fields(data_set=tunes,
                    fields=[
                        NAME_KEY,
                        ARTIST_KEY,
                        LINK_KEY
                    ],
                    type="tune")
except:
    raise ParsingException(f"key: {FILMS_CONTENT_KEY} was not found")