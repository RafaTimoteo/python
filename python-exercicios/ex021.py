from pygame import mixer, event, init

init()
mixer.music.load('ex021.mp3')
mixer.music.play()
event.wait()