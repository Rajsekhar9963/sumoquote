import json


def get_login_credentials():
    with open("/Users/rkosna/Sumoquote_rr/data/login_data.json") as file:
        login_data = json.load(file)
    return [(entry["username"], entry["password"]) for entry in login_data]