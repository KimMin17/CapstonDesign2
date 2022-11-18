import json
import sys
import os

json_count = 0

def make_json(path):
    new_json_obj = {}
    with open(path, "r", encoding = "utf-8") as fr:
        data = json.load(fr)
        new_json_obj["wav"] = data["Data"]["Path"]
        new_json_obj["spk_id"] = data["Data"]["Gender"] + str(data["Data"]["Age"])

    return new_json_obj

def find_json(path, dict):
    global json_count
    try:
        filenames = os.listdir(path)
        for filename in filenames:
            full_path = path + '/' + filename
            if os.path.isdir(full_path):
                find_json(full_path, dict)
            else:
                ext = os.path.splitext(full_path)[-1]
                if ext == '.json':
                    dict["data{}".format(json_count)] = make_json(full_path)
                    json_count += 1

    except PermissionError:
        pass

def make_train_json():
    train_dir = "../data/training/new_label_data"
    train_dict = {}
    
    global json_count
    json_count = 0
    find_json(train_dir, train_dict)
    print("train json all found")

    with open("train.json", "w") as fw:
        json.dump(train_dict, fw)

def make_valid_json():
    valid_dir = "../data/validation/new_label_data"
    valid_dict = {}

    global json_count
    json_count = 0
    find_json(valid_dir, valid_dict)
    print("valid json all found")

    with open("valid.json", "w") as fw:
        json.dump(valid_dict, fw)

def main():
    make_train_json()
    print("train.json done")
    make_valid_json()
    print("valid.json done")

if __name__ == "__main__":
    main()