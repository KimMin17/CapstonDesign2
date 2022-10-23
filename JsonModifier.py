from pathlib import Path
import os
import json
import sys

training_label_data_path = "../data/training/label_data"
validation_label_data_path = "../data/validation/label_data"

training_new_label_data_path = "../data/new_training/label_data"
validation_new_label_data_path = "../data/new_validation/label_data"

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
    pass

def main():
    if len(sys.argv) != 2:
        print("Usage: python JsonModifier.py 'train' or 'validation'")
        return
    
    dirname = None
    wav_dirname = None
    if sys.argv[1] == 'train':
        dirname = "../data/training/label_data"
        wav_dirname = "../data/training/raw_data"
    elif sys.argv[1] == 'validation':
        dirname = "../data/validation/label_data"
        wav_dirname = "../data/validation/raw_data"
    else:
        print("Usage: python JsonModifier.py 'train' or 'validation'")
        return

    find_json(dirname, wav_dirname)

if __name__ == "__main__":
    main()