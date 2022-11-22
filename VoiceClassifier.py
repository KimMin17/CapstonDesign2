import torchaudio
from speechbrain.pretrained import EncoderClassifier

hparam_path = "./results/speaker_id/1986"
wav_path = "./test.wav"

classifier = EncoderClassifier.from_hparams(source=hparam_path, savedir = "pretrained_model")
signal, fs = torchaudio.load(wav_path)

# Compute speaker embeddings
embeddings = classifier.encode_batch(signal)

# Perform classification
output_probs, score, index, text_lab = classifier.classify_batch(signal)

# Posterior log probabilities
print(output_probs)

# Score (i.e, max log posteriors)
print(score)

# Index of the predicted speaker
print(index)

# Text label of the predicted speaker
print(text_lab)