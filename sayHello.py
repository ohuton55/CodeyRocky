import codey, time, rocky, event

@event.start
def on_start():
    codey.emotion.wake_up()
    codey.emotion.look_around()
    codey.display.show('hello', wait = False)
    codey.speaker.play_melody('hello.wav')
    rocky.forward(25, 1)
    codey.display.show_image("000c1010100c000000000c1010100c00")
