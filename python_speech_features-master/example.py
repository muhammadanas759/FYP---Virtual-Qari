#!/usr/bin/env python
import wave
import pyaudioop
from pydub.pydub import AudioSegment
import os
import speech_recognition as sr
from python_speech_features import mfcc
from python_speech_features import delta
from python_speech_features import logfbank
import scipy.io.wavfile as wav
from pydub.pydub.utils import make_chunks

r = sr.Recognizer()
m = sr.Microphone()

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    print("Say something!")
    with m as source: audio = r.listen(source)
except sr.RequestError as e:
    print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))

myaudio=AudioSegment.export(audio,format="wav")
#myaudio = AudioSegment.from_file("english.wav", "wav")
#chunk_length_ms = 1000  # pydub calculates in millisec
#chunks = make_chunks(myaudio, chunk_length_ms)  # Make chunks of one sec

# Export all of the individual chunks as wav files

#for i, chunk in enumerate(chunks):
#    print("chunk{0}.wav features".format(i))
#    chunk_name = "chunk{0}.wav".format(i)
#    print("exporting", chunk_name)
#    chunk.export(chunk_name, format="wav")
#    (rate, sig) = wav.read("chunk{0}.wav".format(i))
#    mfcc_feat = mfcc(sig, rate)
#    d_mfcc_feat = delta(mfcc_feat, 2)
#    fbank_feat = logfbank(sig, rate)
# print("{0},{1}".format(rate,sig))
#    print(fbank_feat[1:3, :])
# print("{0}".format(f.getsampwidth))
