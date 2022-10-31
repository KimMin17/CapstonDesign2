import pathlib
import speechbrain as sb
from hyperpyyaml import load_hyperpyyaml

class XvectorBrain(sb.Brain):
    #brain
    def compute_forward(self, batch, stage):
        pass

    def compute_objectives(self, predictions, batch, stage):
        pass

    def on_stage_start(self, stage, epoch = None):
        pass

    def on_stage_end(self, stage, epoch = None):
        pass

def data_prep(data_folder, hparams):
    #prepare dataset from JSON file
    pass

def main(device = "cpu"):
    #main function
    pass

if __name__ == "__main__":
    main()