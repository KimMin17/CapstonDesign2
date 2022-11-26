from speechbrain.pretrained import EncoderClassifier
import torchaudio

classifier = EncoderClassifier.from_hparams(source = './', hparams_file='inference.yaml', savedir = "./content/best_model/")

# Perform classification
audio_file = 'sound.wav'
signal, fs = torchaudio.load(audio_file)
output_probs, score, index, text_lab = classifier.classify_batch(signal)
print('Predicted: ' + text_lab[0])