from pathlib import Path
import os
import json
import sys

training_label_data_path = "../data/training/label_data/common"
validation_label_data_path = "../data/validation/label_data/common"

training_new_label_data_path = "../data/new_training/label_data/commmon"
validation_new_label_data_path = "../data/new_validation/label_data/commons"

def find_json(dirname, wav_dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = dirname + '/' + filename
            if os.path.isdir(full_filename):
                find_json(full_filename, wav_dirname)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.json': 
                    modify_json(full_filename, wav_dirname)
    except PermissionError:
        pass

def modify_json(path, wav_dirname):
    json_obj = None
    data = {}
    with open(path, 'r', encoding = 'utf-8') as fr:
        json_obj = json.load(fr)
        path_split = path.split("/")
        data["Path"] = wav_dirname + '/' + path_split[-3] + '/' + path_split[-2] + '/' + json_obj["File"]["FileName"]
        data["Gender"] = json_obj["Speaker"]["Gender"]
    
    with open(path, 'w', encoding = 'utf-8') as fw:
        pass

def main():
    if len(sys.argv) != 2:
        print("Usage: python JsonModifier.py 'train' or 'validation'")
        return
    
    dirname = None
    wav_dirname = None
    if sys.argv[1] == 'train':
        dirname = "../data/training/label_data/common"
        wav_dirname = "../data/training/raw_data/common"
    elif sys.argv[1] == 'validation':
        dirname = "../data/validation/label_data/common"
        wav_dirname = "../data/validation/raw_data/common"
    else:
        print("Usage: python JsonModifier.py 'train' or 'validation'")
        return

    find_json(dirname, wav_dirname)

if __name__ == "__main__":
    main()