# pyttsx3-tts

Requirement(s)
1. have pyttsx3 on your python
  - to install
    pip install pyttsx3
2. Windows(?)

All functions are stored in the tts.py and can be run using the run.py

function descriptions:

1. get(name)
  -get the value of the current setting
  -the name input is a string
  -possible value for name: 'rate', 'voice', 'voices', 'volume'
  -rate: the speed that the voice is currently speaking in (in word per minute)
  -voice: the voice that is currently in used
  -voices: all the possible voice that can be selected
  -volume: the loudness of the current speech setting (value between 0.0-1.0)
  -NOTE: this function is a shortened form of engine.getProperty(name) which is made for convenience check out the ref for more info

2. volume(volume)
  - set the speech loudness (the volume attribute) equal to the input volume
  - volume is a float
  - input range = [0.0-1.0]
  - default value = 1.0

3. rate(rate)
  - set the speech speed (the rate attribute) equal to rate in wpm
  - rate is an int
  - default value = 200 wpm
  - FYI wpm = word per minute
  
4. voice(voice)
  - set the voice used for speech to be one with the same index as given 
  - voice is an int that represents the index of the voice object in the voices list
  - call print_index to check the index number (6.), and test_voice(msg="") (7.) to cheeck the sound

5. say(msg)
  - read the msg outloud using the current setting (can be viiew using get)

6. print_index()
  - print out the indexes and names of all the voices
  - the indexes are useful when trying to set the voices using voice(voice) (4.)
  
7. test_voice(msg="")
  - print and speak out loud the name, index, and the given msg in all availible voices
  - msg is a string that default to ""
  
8. get_all()
  - print out all the current setting

  
ref: https://pyttsx3.readthedocs.io/en/latest/engine.html
