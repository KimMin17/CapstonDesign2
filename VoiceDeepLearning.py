import glob
import json
import os
import torchaudio
from pathlib import Path
from speechbrain.dataio.dataset import DynamicItemDataset

training_raw_data_path = "../data/training/raw_data/common"
training_label_data_path = "../data/training/label_data/common"
validation_raw_data_path = "../data/validation/raw_data/common"
validation_label_data_path = "../data/validation/label_data/common"

json_file_list = []
def search_json_file(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search_json_file(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.json': 
                    json_file_list.append(full_filename)
                    #print(full_filename)
    except PermissionError:
        pass

def make_data_loader(json_file_list):
    pass


def main():
    pass

if __name__ == "__main__":
    main()