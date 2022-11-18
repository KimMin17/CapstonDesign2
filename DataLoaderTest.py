import glob
import json
import os
from pathlib import Path
from speechbrain.dataio.dataset import DynamicItemDataset
import speechbrain

@speechbrain.utils.data_pipeline.takes("wav")
@speechbrain.utils.data_pipeline.provides("sig")
def audio_pipeline(wav):
      sig = speechbrain.dataio.dataio.read_audio(wav)
      return sig

def make_dataset(json_file):
    dataset = DynamicItemDataset.from_json(json_file)
    dataset.add_dynamic_item(audio_pipeline)
    dataset.set_output_keys(["sig"])

    print(len(dataset))

def main():
    make_dataset("./train.json")

if __name__ == "__main__":
    main()