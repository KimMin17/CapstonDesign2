from pathlib import Path
import os
import json
import sys

training_label_data_path = "../data/training/label_data/common"
validation_label_data_path = "../data/validation/label_data/common"

def find_json(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = dirname + '/' + filename
            if os.path.isdir(full_filename):
                find_json(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.json': 
                    modify_json(full_filename, dirname)
    except PermissionError:
        pass

def modify_json(path, dirname):
    json_obj = None
    with open(path, 'r', encoding = 'utf-8') as fr:
        json_obj = json.load(fr)
        json_obj['File']['DirectoryPath'] = dirname
    
    with open(path, 'w', encoding = 'utf-8') as fw:
        json.dump(json_obj, fw, indent = '\t', ensure_ascii=False)

def main():
    if len(sys.argv) != 2:
        print("Usage: python JsonModifier.py 'train' or 'validation'")
        return
    if sys.argv[1] == 'train':
        dirname = "../data/training/label_data/common"
    elif sys.argv[1] == 'validation':
        dirname = "../data/validation/label_data/common"
    else:
        print("Usage: python JsonModifier.py 'train' or 'validation'")
        return

    find_json(dirname)

if __name__ == "__main__":
    main()