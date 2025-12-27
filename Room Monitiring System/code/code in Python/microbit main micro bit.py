def on_received_value(name, value):
    global Tc_1, humidity_1, smoke_1, Tc_2, humidity_2, Smoke_2
    if name == "TC 1":
        Tc_1 = value
    elif name == "hum 1":
        humidity_1 = value
    elif name == "smoke 1":
        smoke_1 = value
    elif name == "TC 2":
        Tc_2 = value
    elif name == "hum 2":
        humidity_2 = value
    elif name == "smoke 2":
        Smoke_2 = value
radio.on_received_value(on_received_value)

average_humidity = 0
average_smoke = 0
average_Tc = 0
Smoke_2 = 0
humidity_2 = 0
Tc_2 = 0
smoke_1 = 0
humidity_1 = 0
Tc_1 = 0
radio.set_group(10)
I2C_LCD1602.lcd_init(39)

def on_forever():
    global average_Tc, average_smoke, average_humidity
    average_Tc = (Tc_1 + Tc_2) / 2
    average_smoke = (smoke_1 + Smoke_2) / 2
    average_humidity = (humidity_1 + humidity_2) / 2
    I2C_LCD1602.show_string("Tc =", 0, 0)
    I2C_LCD1602.show_number(average_Tc, 6, 0)
    basic.pause(5000)
    I2C_LCD1602.clear()
    I2C_LCD1602.show_string("humidity =", 0, 0)
    I2C_LCD1602.show_number(average_humidity, 13, 0)
    basic.pause(5000)
    I2C_LCD1602.clear()
    I2C_LCD1602.show_string("smoke =", 0, 0)
    I2C_LCD1602.show_number(average_smoke, 10, 0)
    basic.pause(5000)
    I2C_LCD1602.clear()
    if average_Tc <= 24:
        # red led 1 is on
        pins.digital_write_pin(DigitalPin.P0, 1)
    if average_smoke >= 20:
        # red led 2 is on
        pins.digital_write_pin(DigitalPin.P1, 1)
    if average_humidity < 50:
        # red led 3 is on
        pins.digital_write_pin(DigitalPin.P2, 1)
basic.forever(on_forever)
