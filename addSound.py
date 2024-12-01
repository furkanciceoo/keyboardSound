from pynput.keyboard import Listener, Key
from pygame import mixer



def play():
    mixer.init()
    mixer.music.load(r'C:\Users\Furkan\Downloads\4380\4380.MP3')
    mixer.music.play()

def on_press(key):
    try:
        # Boşluk tuşu kontrolü
        if key == Key.space:
            play()
    except AssertionError:
        pass

with Listener(on_press=on_press) as listener:
    listener.join()
