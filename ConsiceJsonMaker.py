import sys
import json

def create_simple_json(json_file, data_num):
    json_obj = {}
    new_json_obj = {}

    m_list = ["M3", "M4", "M5"]
    f_list = ["F3", "F4", "F5"]
    c_list = ["M1", "M2", "F1", "F2"]

    counter = 0
    m_counter = 0
    f_counter = 0
    c_counter = 0

    with open(json_file, "r") as fr:
        json_obj = json.load(fr)

    for key, value in json_obj.items():
        if value["spk_id"] in m_list:
            if m_counter >= data_num: continue
            new_json_obj["data{}".format(counter)] = {}
            new_json_obj["data{}".format(counter)]["wav"] = value["wav"]
            new_json_obj["data{}".format(counter)]["spk_id"] = "M"
            m_counter += 1
            counter += 1
            
        elif value["spk_id"] in f_list:
            if f_counter >= data_num: continue
            new_json_obj["data{}".format(counter)] = {}
            new_json_obj["data{}".format(counter)]["wav"] = value["wav"]
            new_json_obj["data{}".format(counter)]["spk_id"] = "F"
            f_counter += 1
            counter += 1

        elif value["spk_id"] in c_list:
            if c_counter >= data_num: continue
            new_json_obj["data{}".format(counter)] = {}
            new_json_obj["data{}".format(counter)]["wav"] = value["wav"]
            new_json_obj["data{}".format(counter)]["spk_id"] = "C"
            c_counter += 1
            counter += 1

        if counter >= 3 * data_num: break

    with open("./simple_" + json_file, "w") as fw:
        json.dump(new_json_obj, fw)

def main():
    train = "train.json"
    valid = "valid.json"
    test = "test.json"

    create_simple_json(train, 1000)
    create_simple_json(valid, 300)
    create_simple_json(test, 100)

if __name__ == "__main__":
    main()