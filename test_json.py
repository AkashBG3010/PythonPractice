import json


def json_operation(filename = 'data.json'):
    with open(filename, 'r+') as file:
        data = json.load(file)

        data["resource1"][0]["total_price"] = "1750"
        data["resource2"][0]["total_price"] = "725"
        data["resource3"][0]["total_price"] = "250"

        file.seek(0)

        json.dump(data, file, indent = 4)


if __name__ == '__main__':

    json_operation()

print("------End of program------")
