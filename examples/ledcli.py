#!/usr/bin/python

import sys
import getopt

import max7219.font as font
import max7219.led as led


def showtext(text, mode, bright):
    device = led.matrix(cascaded=1)
    device.flush()

    print bright
    device.brightness(bright)
    device.show_message(text, font=font.SINCLAIRS_FONT)
    device.flush()

def main(argv):
    text = None
    mode = 'rtl'
    bright = 5
    try:
        opts, args = getopt.getopt(argv, "hbt:m", ["text=", "mode=", "bright="])
    except getopt.GetoptError:
        print 'ledcli.py -t <text> -m <mode> -b <brightness>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'ledcli.py -t <text> -m <mode>'
            sys.exit()
        elif opt in ("-t", "--text"):
            text = arg
        elif opt in ("-m", "--mode"):
            mode = arg
        elif opt in ("-b", "--bright"):
            bright = int(arg)

    if mode is None:
        print 'No text given. Stupid.'
    else:
        showtext(text, mode, bright)

if __name__ == "__main__":
    main(sys.argv[1:])