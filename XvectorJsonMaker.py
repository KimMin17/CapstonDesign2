import os
import json

spk_train_raw_path = "../content/spk_rec/training/raw_data"
spk_train_label_path = "../content/spk_rec/training/label_data"
spk_valid_raw_path = "../content/spk_rec/validation/raw_data"
spk_valid_label_path = "../content/spk_rec/validation/label_data"
spk_test_label_path = "../content/spk_rec/validation/test_label_data"

chd_train_raw_path = "../content/chd_rec/training/raw_data"
chd_train_label_path = "../content/chd_rec/training/label_data"
chd_valid_raw_path = "../content/chd_rec/validation/raw_data"
chd_valid_label_path = "../content/chd_rec/validation/label_data"
chd_test_label_path = "../content/chd_rec/validation/test_label_data"

def make_wav_path(path):
    if "test_label" in path: return path.replace("test_label", "raw").replace(".json", ".wav")
    else: return path.replace("label", "raw").replace(".json", ".wav")

def make_json_obj_from_path(json_path, type):
    new_json_obj = {}
    new_json_obj["wav"] = make_wav_path(json_path)
    with open(json_path, "r", encoding="utf-8") as fr:
        json_obj = json.load(fr)
        if type == "spk":
            if json_obj["Speaker"]["Gender"] == "Male": new_json_obj["spk_id"] = "M"
            else: new_json_obj["spk_id"] = "F"
        elif type == "chd": new_json_obj["spk_id"] = "C"
    
    return new_json_obj

def make_json_obj_list(type, data_num):
    data_num_per_spk = 2
    json_obj_list = []
    json_obj_count = 0

    root_path = ""
    if type == "spk_train": root_path = spk_train_label_path
    elif type == "spk_valid": root_path = spk_valid_label_path
    elif type == "spk_test": root_path = spk_test_label_path
    elif type == "chd_train": root_path = chd_train_label_path
    elif type == "chd_valid": root_path = chd_valid_label_path
    elif type == "chd_test": root_path = chd_test_label_path
    else:
        print("something wrong with data type")
        exit()

    date_folders = os.listdir(root_path)
    for date_folder in date_folders:
        spk_folders = os.listdir(root_path + '/' + date_folder)
        for spk_folder in spk_folders:
            spk_files = os.listdir(root_path+'/'+date_folder+'/'+spk_folder)
            folder_len = len(spk_files)
            for i in range(min(folder_len, data_num_per_spk)):
                json_obj_list.append(root_path+'/'+date_folder+'/'+spk_folder+'/'+spk_files[i])
                json_obj_count += 1

                if json_obj_count >= data_num: break
            if json_obj_count >= data_num: break
        if json_obj_count >= data_num: break
    
    return json_obj_list


def create_json_file(json_file, data_num):
    json_dict = {}

    spk_json_list = []
    chd_json_list = []

    each_data_num = data_num // 2

    if "train" in json_file:
        spk_json_list = make_json_obj_list("spk_train", each_data_num)
        chd_json_list = make_json_obj_list("chd_train", each_data_num)
    elif "valid" in json_file:
        spk_json_list = make_json_obj_list("spk_valid", each_data_num)
        chd_json_list = make_json_obj_list("chd_valid", each_data_num)
    elif "test" in json_file:
        spk_json_list = make_json_obj_list("spk_test", each_data_num)
        chd_json_list = make_json_obj_list("chd_test", each_data_num)

    count = 0

    for spk_json in spk_json_list:
        json_dict["data{}".format(count)] = make_json_obj_from_path(spk_json, "spk")
        count += 1

    for chd_json in chd_json_list:
        json_dict["data{}".format(count)] = make_json_obj_from_path(chd_json, "chd")
        count += 1

    with open(json_file, "w") as fw:
        json.dump(json_dict, fw)

def main():
    train = "new_train.json"
    valid = "new_valid.json"
    test = "new_test.json"

    train_data_num = 3000
    valid_data_num = 900
    test_data_num = 300

    create_json_file(train, train_data_num)
    create_json_file(valid, valid_data_num)
    create_json_file(test, test_data_num)

if __name__ == "__main__":
    main()