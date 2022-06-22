#!/usr/bin/env python3

# Imports
from tensorflow.lite import vision

from tflite_support.task import vision
from tflite_support.task import core
from tflite_support.task import processor

default_dir = os.getcwd()
model_path = default_dir + '/soundclassifier_with_metadata.tflite'
print(f'Data directory will be: {model_path}')

# Initialization
base_options = core.BaseOptions(file_name=model_path)
classification_options = processor.ClassificationOptions(max_results=2)
options = audio.AudioClassifierOptions(base_options=base_options, classification_options=classification_options)
classifier = audio.AudioClassifier.create_from_options(options)

# Alternatively, you can create an audio classifier in the following manner:
# classifier = audio.AudioClassifier.create_from_file(model_path)

# Run inference
audio_file = audio.TensorAudio.create_from_wav_file(audio_path, classifier.required_input_buffer_size)
audio_result = classifier.classify(audio_file)
