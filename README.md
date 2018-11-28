# Naver TTS API

This script uses the Naver TTS API (found on e.g. papago.naver.com) to produce the pronunciation
for a given Korean phrase and saves it as an mp3 file.

I use this for automating the process of adding pronunciation samples to electronic flashcards.

For testing purposes, the script defaults to playing the mp3 after downloading it. Once you've
confirmed it works, comment out the last line to just download the file without playing it.

## Usage

`python naver.py [TEXT] [OUT_FILE.MP3]`

## Example

`python naver.py "헬로우 월드" hello.mp3`
