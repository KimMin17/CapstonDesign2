from pathlib import Path
import os
import json
import sys

training_label_data_path = "../data/training/label_data/common"
validation_label_data_path = "../data/validation/label_data/common"

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
    with open(path, 'r', encoding = 'utf-8') as fr:
        json_obj = json.load(fr)
        path_split = path.split("/")
        json_obj['path'] = wav_dirname + '/' + path_split[-3] + '/' + path_split[-2] + '/' + json_obj["File"]["FileName"]
    
    with open(path, 'w', encoding = 'utf-8') as fw:
        json.dump(json_obj, fw, indent = '\t')

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