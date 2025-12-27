Smoke = 0
humidity = 0
Tc = 0
radio.set_group(10)

def on_every_interval():
    global Tc, humidity, Smoke
    Tc = input.temperature()
    radio.send_value("TC 2", Tc)
    basic.pause(100)
    humidity = pins.analog_read_pin(AnalogReadWritePin.P0)
    radio.send_value("hum 2", humidity)
    basic.pause(100)
    Smoke = pins.analog_read_pin(AnalogReadWritePin.P2)
    radio.send_value("smoke 2", Smoke)
loops.every_interval(360000, on_every_interval)
