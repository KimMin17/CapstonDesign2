import glob
import json
import os
from pathlib import Path
from speechbrain.dataio.dataset import DynamicItemDataset
import speechbrain

@speechbrain.utils.data_pipeline.takes("file_path")
@speechbrain.utils.data_pipeline.provides("signal")
def audio_pipeline(file_path):
      sig = speechbrain.dataio.dataio.read_audio(file_path)
      return sig

def make_dataset(json_file):
    dataset = DynamicItemDataset.from_json(json_file)
    dataset.add_dynamic_item(audio_pipeline)
    dataset.set_output_keys(["signal"])
    print(dataset[0])

def main():
    make_dataset("./data.json")

if __name__ == "__main__":
    main()