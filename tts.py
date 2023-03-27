import pyttsx3

# engine setup
engine = pyttsx3.init()

# get the value of the current setting, possible parameters: 'rate', 'voice', 'voices', 'volume'
get = engine.getProperty

# say the msg outloud using the current setting
def say(msg):
    engine.say(msg)
    engine.runAndWait()

# set the speech loudness (the volume attribute) equal to volume, input range = [0.0-1.0], default = 1.0
def volume(volume):
    engine.setProperty('volume',volume)

# set the speech speed (the rate attribute) equal to rate in wpm, default = 200
def rate(rate):
    engine.setProperty('rate',rate)

# set the voice to be the voice with the same index as given 
# (call print_index to check the index number, and test_voice to cheeck the sound)
def voice(index):
    voices = get('voices')
    id = voices[index].id
    engine.setProperty('voice',id)

# print out the indexes and names of all the voices
def print_index():
    i = 0
    print(f"index\tName")
    for voice in get('voices'):
        print(f"{i}\t{voice.name}")
        i+=1

# print and speak out loud the name, index, and the given msg, which is "" by default, in all availible voices
def test_voice(msg=""):
    i = 0
    for voice_ in get('voices'):
        voice(i)        
        print(f"Hello my name is {voice_.name}, my index is {i} {msg}")
        say(f"Hello my name is {voice_.name}, my index is {i} {msg}")
        i+=1

# get all the current setting property
def get_all():
    PROPERTY = ['rate','voice','voices','volume']
    print('--------------------------------------------------------------------------------------------')
    for i in PROPERTY:
        print(f"{i}: {get(i)}")
        print('--------------------------------------------------------------------------------------------')


