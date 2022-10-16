import glob
import json
import os
from pathlib import Path
from speechbrain.dataio.dataset import DynamicItemDataset
import speechbrain

training_raw_data_path = "../data/training/raw_data/common"
training_label_data_path = "../data/training/label_data/common"
validation_raw_data_path = "../data/validation/raw_data/common"
validation_label_data_path = "../data/validation/label_data/common"

json_file_list = []
def search_json_file(dirname,):
    global json_file_list
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = dirname + '/' + filename
            if os.path.isdir(full_filename):
                search_json_file(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.json': 
                    json_file_list.append(full_filename)
    except PermissionError:
        pass

@speechbrain.utils.data_pipeline.takes("path")
@speechbrain.utils.data_pipeline.provides("signal")
def audio_pipeline(path):
      sig = speechbrain.dataio.dataio.read_audio(path)
      return sig

def make_dataset(json_file):
    dataset = DynamicItemDataset.from_json(json_file)
    #dataset.add_dynamic_item(audio_pipeline)
    #dataset.set_output_keys(["signal"])
    print(dataset[0])

def main():
    global json_file_list
    search_json_file("../data/training/label_data/common")
    print(len(json_file_list))
    make_dataset(json_file_list[0])

if __name__ == "__main__":
    main()