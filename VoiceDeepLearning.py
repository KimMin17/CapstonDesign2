import os
from speechbrain.dataio.dataset import DynamicItemDataset
import speechbrain

@speechbrain.utils.data_pipeline.takes("Path")
@speechbrain.utils.data_pipeline.provides("Signal")
def audio_pipeline(path):
      sig = speechbrain.dataio.dataio.read_audio(path)
      return sig

def make_dataset(json_file):
    dataset = DynamicItemDataset.from_json(json_file)
    dataset.add_dynamic_item(audio_pipeline)
    dataset.set_output_keys(["Signal", "Age", "Gender"])
    print(dataset[0])

def voice_learning(json_file):
    make_dataset(json_file)

def search_json_file(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = dirname + '/' + filename
            if os.path.isdir(full_filename):
                search_json_file(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.json':
                    voice_learning(full_filename)
    except PermissionError:
        pass

def main():

    training_raw_data_path = "../data/training/raw_data"
    training_label_data_path = "../data/training/new_label_data"
    validation_raw_data_path = "../data/validation/raw_data"
    validation_label_data_path = "../data/validation/new_label_data"

    test_json_file = "../data/training/new_label_data/training_label_data_0/training_label_data_0_0.json"

    voice_learning(test_json_file)

if __name__ == "__main__":
    main()