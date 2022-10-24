import os
import torch
from speechbrain.dataio.dataset import DynamicItemDataset
import speechbrain as sb

class VoiceBrain(sb.Brain):
    def compute_forward(self, batch, stage):
        pass

    def compute_objectives(self, batch, stage):
        pass

@sb.utils.data_pipeline.takes("Path")
@sb.utils.data_pipeline.provides("Signal")
def audio_pipeline(path):
      sig = sb.dataio.dataio.read_audio(path)
      return sig

def make_dataset(json_file):
    dataset = DynamicItemDataset.from_json(json_file)
    dataset.add_dynamic_item(audio_pipeline)
    dataset.set_output_keys(["Signal", "Age", "Gender"])

    input_size = 8000
    tensor_size = dataset[0]["Signal"].size()[0]
    padding_size = (tensor_size // input_size + 1) * input_size - tensor_size

    padding_tensor = torch.zeros(padding_size)
    print(padding_tensor.size())

    dataset[0]["Signal"] = torch.cat([dataset[0]["Signal"], padding_tensor], dim = 0)

    print(dataset[0]["Signal"].size())

def model_learning():
    pass

def voice_learning(json_file):
    make_dataset(json_file)
    model_learning()

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