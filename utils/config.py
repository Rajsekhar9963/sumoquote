import json


def get_data():
    with open("data/create_account_data.json") as file:
        create_account_data = json.load(file)
    return [(entry["url"], entry["organization_name"], entry["first_name"], entry["last_name"], entry["email"], entry["phone_number"], entry["password"], entry["ad_option"]) for entry in create_account_data]