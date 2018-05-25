import machine, neopixel, time
#Connect Data to D5 for Pin 14

np = neopixel.NeoPixel(machine.Pin(14), 1) # One LED on GPIO 4

while True:
	np[0] = (255, 0, 0) # set to red, full brightness
	np.write()
	time.sleep_ms(500)
	np[0] = (255, 255, 0) # set to red, full brightness
	np.write()
	time.sleep_ms(500)
	np[0] = (255, 255, 255) # set to red, full brightness
	np.write()
	time.sleep_ms(500)
	np[0] = (0, 255, 0) # set to red, full brightness
	np.write()
	time.sleep_ms(500)
	np[0] = (0, 0, 255) # set to red, full brightness
	np.write()
	time.sleep_ms(500)
