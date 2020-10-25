import json
import os


def main():
    with open("C:/Users/Jacob Snyderman/PycharmProjects/UBHacking-2020/data/google_keys.json") as f:
        json_str = dict(json.loads(f.read()))["web"]
        os.environ["GOOGLE_CLIENT_ID"] = json_str["client_id"]
        os.environ["GOOGLE_CLIENT_SECRET"] = json_str["client_secret"]

    with open("C:/Users/Jacob Snyderman/PycharmProjects/UBHacking-2020/data/serverKey.json") as w:
        json_str2 = dict(json.loads(w.read()))
        os.environ["APP_SECRET_KEY"] = json_str2["SERVER_KEY"]
        os.environ["API_KEY"] = json_str2["API_KEY"]
        os.environ["DB_PASS"] = json_str2["DB_PASSWORD"]


if __name__ == '__main__':
    main()
