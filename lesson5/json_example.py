import json
from turtle import pu


def example_data_manipulation():
    example_json_str = """
        {
          "squadName": "Super hero squad",
          "homeTown": "Metro City",
          "formed": 2016,
          "secretBase": "Super tower",
          "active": true,
          "members": [
            {
              "name": "Molecule Man",
              "age": 29,
              "secretIdentity": "Dan Jukes",
              "powers": [
                "Radiation resistance",
                "Turning tiny",
                "Radiation blast"
              ]
            },
            {
              "name": "Madame Uppercut",
              "age": 39,
              "secretIdentity": "Jane Wilson",
              "powers": [
                "Million tonne punch",
                "Damage resistance",
                "Superhuman reflexes"
              ]
            },
            {
              "name": "Eternal Flame",
              "age": 1000000,
              "secretIdentity": "Unknown",
              "powers": [
                "Immortality",
                "Heat Immunity",
                "Inferno",
                "Teleportation",
                "Interdimensional travel"
              ]
            }
          ]
        }"""
    json2_str = '{ "key" : "value"}'

    json_example_obj = json.loads(json2_str)
    # print(json_example_obj)
    json_text = json.dumps(json_example_obj, indent=2)
    print(json_text)

    json_example_obj["key"] = "new value"
    print(json.dumps(json_example_obj, indent=2))
    json_example_obj["key2"] = "value"
    print(json.dumps(json_example_obj, indent=2))

    example_list = ["nick", "dima", "ladimir"]
    json_example_obj["listeners"] = example_list
    print(json.dumps(json_example_obj, indent=2))


def example_save_json_to_file(file_path):
    json2_str = '{}'
    json_example_obj = json.loads(json2_str)
    json_example_obj["key"] = "new value"
    json_example_obj["key2"] = "value"
    example_list = ["nick", "dima", "ladimir"]
    json_example_obj["listeners"] = example_list

    print("save json to file")
    with open(file_path, "wt") as f:
        json.dump(json_example_obj, f, indent=2)

def example_read():
    file_path = "example.json"
    example_save_json_to_file(file_path)
    print("read json from file")
    with open(file_path, "r") as f:
        json_object = json.load(f)
    print(json.dumps(json_object, indent=3))


def main():
    pass
    pupol = dict()
    pupol["name"] = "Nick"
    pupol["age"] = 32
    pupol["hobby_list"] = ["prgramming", "woodworking", "fishing"]

    json_obj = json.loads("{}")
    json_obj["pupol"] = pupol
    print(json.dumps(json_obj, indent=2))

    xml = """
<xml document>
<root name="document root" readonly="true" type="string">
    <Pupol></Pupol>    
    <Pupol></Pupol>
</root>
<?xml>
"""


if __name__ == '__main__':
    main()
