#!/usr/bin/env python3
import queue
import sounddevice as sd
import vosk
import json
from vosk import Model, KaldiRecognizer

q = queue.Queue()

model=vosk.Model('./model/vosk-model-uk-v3')

device = sd.default.device
samplerate = int(sd.query_devices(device[1], 'input')['default_samplerate'])

def callback(indata, frames, time, status):

    q.put(bytes(indata))

with sd.RawInputStream(samplerate=samplerate, blocksize = 8000, device=device[1],
        dtype="int16", channels=1, callback=callback):
    
    rec = KaldiRecognizer(model, samplerate)
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            data = json.loads(rec.Result())['text']
            print(data)
        # else:
        #     print(rec.PartialResult())


