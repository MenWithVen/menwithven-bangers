from src.service import update_json_bollocks, TUNES_JSON_FILEPATH, FILMS_JSON_FILEPATH, FILMS_CONTENT_KEY, \
    TUNES_CONTENT_KEY, NAME_KEY, ARTIST_KEY, LINK_KEY, ON_NETFLIX_KEY, ON_PRIME_KEY

print("what type of banger do u want to add?\n- tune\n- film")
type = input()


if type == "film":
    print("film name?")
    name = input()

    print("link?")
    link = input()

    print("on netflix?")
    on_netflix = input()

    print("on prime?")
    on_prime = input()

    update_json_bollocks(file_path=FILMS_JSON_FILEPATH,
                         args={NAME_KEY: name,
                               LINK_KEY: link,
                               ON_NETFLIX_KEY: on_netflix,
                               ON_PRIME_KEY: on_prime},
                         key=FILMS_CONTENT_KEY)

elif type == "tune":
    print("tune name?")
    name = input()

    print("artist?")
    artist = input()

    print("link?")
    link = input()

    update_json_bollocks(file_path=TUNES_JSON_FILEPATH,
                         args={NAME_KEY: name,
                               ARTIST_KEY: artist,
                               LINK_KEY: link},
                         key=TUNES_CONTENT_KEY)

else:
    raise Exception("invalid input bud")