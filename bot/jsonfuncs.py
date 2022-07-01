import os
import json


def add_bees(msg: int, bees: float):
    if os.path.isfile("bees.json"):
        # Opens file and loads the data.
        with open("bees.json", "r") as bee:
            data = json.load(bee)
        # Adds points if group already exists.
        try:
            data[f"{msg}"] += bees
        # Creates a new group and adds points if group doesnt exist
        except KeyError:
            data[f"{msg}"] = bees
    else:
        data = {f"{msg}": bees}
    # Saves file to store the data.
    with open("bees.json", "w+") as bee:
        json.dump(data, bee, sort_keys=True, indent=4)


def view_bees(msg: int):
    with open("bees.json", "r") as votes:
        data = json.load(votes)
    try:
        response = data[f"{msg}"]
    except Exception as e:
        print(e)
        response = 0
    return response
        
