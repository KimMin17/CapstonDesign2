import os
import json
import sys

def find_json(path, new_path, wav_path):
    try:
        filenames = os.listdir(path)
        for filename in filenames:
            full_path = path + '/' + filename
            if os.path.isdir(full_path):
                find_json(full_path, new_path, wav_path)
            else:
                ext = os.path.splitext(full_path)[-1]
                if ext == '.json': 
                    make_new_json(full_path, new_path, wav_path)
    except PermissionError:
        pass

def make_new_json(path, new_path, wav_path):
    new_json_obj = {"Data" : {}}
    file_name = path.split("/")[-1]
    folder_name = path.split("/")[-2]
    
    full_new_path = new_path + '/' + folder_name + '/' + file_name
    full_wav_path = wav_path + '/' + folder_name + '/' + file_name.split(".")[0] + ".wav"

    new_json_obj["Data"]["Path"] = full_wav_path

    with open(path, "r", encoding = "utf-8") as fr:
        data = json.load(fr)
        if data["녹음자정보"]["gender"] == "여":
            new_json_obj["Data"]["Gender"] = "F"
        else:
            new_json_obj["Data"]["Gender"] = "M"
        new_json_obj["Data"]["Age"] = data["녹음자정보"]["age"] // 10

    #for key, value in new_json_obj.items():
    #    print(key, ":", value)

    try:
        if not os.path.exists(new_path + '/' + folder_name):
            os.makedirs(new_path + '/' + folder_name)
    except OSError:
        pass

    with open(full_new_path, "w+") as fw:
        json.dump(new_json_obj, fw)


def main():
    if len(sys.argv) != 2:
        print("Usage: python JsonModifier.py 'train' or 'validation'")
        return

    training_label_data_path = "../data/training/label_data"
    training_new_label_data_path = "../data/training/new_label_data"
    training_raw_data_path = "../data/training/raw_data"

    validation_label_data_path = "../data/validation/label_data"
    validation_new_label_data_path = "../data/validation/new_label_data"
    validation_raw_data_path = "../data/validation/raw_data"
    
    path = None
    new_path = None
    wav_path = None

    if sys.argv[1] == 'train':
        path = training_label_data_path
        new_path = training_new_label_data_path
        wav_path = training_raw_data_path
    elif sys.argv[1] == 'validation':
        path = validation_label_data_path
        new_path = validation_new_label_data_path
        wav_path = validation_raw_data_path
    else:
        print("Usage: python JsonModifier.py 'train' or 'validation'")
        return
    
    find_json(path, new_path, wav_path)

if __name__ == "__main__":
    main()