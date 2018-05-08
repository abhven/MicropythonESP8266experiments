import machine, neopixel
#Connect Data to D5 for Pin 14

np = neopixel.NeoPixel(machine.Pin(14), 1) # One LED on GPIO 4
np[0] = (255, 0, 0) # set to red, full brightness
np.write()