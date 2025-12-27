# micro bit 2

def on_received_number(receivedNumber):
    if receivedNumber == 2:
        # water pump
        pins.digital_write_pin(DigitalPin.P1, 1)
        # wait 5 min before it turn of
        basic.pause(30000)
        # water pump
        pins.digital_write_pin(DigitalPin.P1, 0)
    else:
        # water pump
        pins.digital_write_pin(DigitalPin.P1, 0)
radio.on_received_number(on_received_number)

temperature = 0
humidity = 0
radio.set_group(10)
# micro bit 1

def on_forever():
    global humidity, temperature
    humidity = pins.analog_read_pin(AnalogReadWritePin.P0)
    if humidity < 40:
        radio.send_number(2)
    temperature = input.temperature()
    if temperature < 20:
        temperature = 20
    elif temperature > 35:
        temperature = 35
    pins.servo_write_pin(AnalogPin.P1, pins.map(temperature, 20, 35, 0, 180))
basic.forever(on_forever)
