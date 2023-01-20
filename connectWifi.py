# generated by mBlock5 for codey & rocky
# codes make you happy
import codey, event, time, uos
import urequests as requests
import utime

class Setting():
    def __init__(self):
        codey.speaker.volume = 10

    def connectWifi(self):
        ssid = 'Rakuten-6F13'
        password = '6U622R2F84'
        ntp_host = 'ntp.nict.jp'
        res = ''
        codey.wifi.start(ssid, password, codey.wifi.STA)
        time.sleep(3)
        if codey.wifi.is_connected():
            codey.emotion.smile()
            res = requests.get(url = 'http://nururi.syanari.com').text
            codey.display.show('myIP:' + res, wait=False)
        else:
            codey.emotion.shiver()

class Moving(Setting):
    @event.button_a_pressed
    def on_button_a_pressed():
        codey.speaker.play_melody('hello.wav')
        codey.display.show_image("00003c7e7e3c000000003c7e7e3c0000") 
        codey.display.show(utime.localtime(), wait = True)

    @event.button_b_pressed
    def on_button_b_pressed1():
        codey.speaker.play_melody('yeah.wav')
        codey.display.show_image("000c18181c0c000000000c1c18180c00")
        h = 20
        m = 40
        s = 0
        msg = str(h) +':'+ str(m)
        codey.display.show(msg, wait = False)
        for i in range(0, 604800, 1):
            time.sleep(0.97)
            s += 1
            if s % 60 == 0:
                s = 0
                m += 1
                if m % 60 == 0:
                    codey.emotion.proud()
                    m = 0
                    h += 1
                    if h % 24 == 0:
                        h = 0
            if s % 2 == 0:
                msg = str(h) + ';' + str(m)
            else:
                msg = str(h) + ':' + str(m)
            codey.display.show(msg, wait = False)
        
    @event.button_c_pressed
    def on_button_c_pressed2():
        codey.speaker.play_melody('sad.wav')
        codey.display.show_image("00000c1e3e3c000000003c3e1e0c0000")
        codey.display.show(uos.uname().sysname)
        
s = Setting()          
s.connectWifi()
Moving()