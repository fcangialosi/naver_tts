#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, json
import requests
import base64

# note: request *should* be of the form 'alphak'
ENCODE_BEGIN = b'\xaeU\xae\xa1C\x9b,Uzd\xf8\xef'
ENCODE_END   = b'"}'
def encode(text, pitch=0, speed=2, voice="kyuri"):
    params = 'pitch":{},"speaker":{},"speed":{},"text":"'.format(
            pitch, 
            "\"{}\"".format(voice),
            speed
    ).encode('utf-8')
    s = ENCODE_BEGIN + params + text.encode('utf-8') + ENCODE_END
    return base64.b64encode(s)

def get_id(data):
    r = requests.post('https://papago.naver.com/apis/tts/makeID', {'data' : data })
    return r.text

def get_audio(tts_id):
    r = requests.get('https://papago.naver.com/apis/tts/{}'.format(tts_id))
    return r.content

# first arg = korean text
text = unicode(sys.argv[1], 'utf-8') 
# second arg = mp3 output file (e.g. test.mp3)
outfile = sys.argv[2]
# encode the full request as base64
encoded = encode(text)
# part 1: get the TTS id 
res = get_id(encoded)
tts_id = json.loads(res)['id']
# part 2: get the audio for this id
audio = get_audio(tts_id)
# save the audio to a file
with open(outfile, 'wb') as f:
    f.write(audio)
# play file (works on OS X)
os.system("play {}".format(outfile))
