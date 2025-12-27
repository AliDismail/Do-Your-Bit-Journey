Tc = 0
humidity = 0
fog_constant = 0
motion_1 = 0
motion_2 = 0
light2 = 0

def on_every_interval():
    I2C_LCD1602.show_string("Tc:", 0, 0)
    I2C_LCD1602.show_number(Tc, 6, 0)
    I2C_LCD1602.clear()
    I2C_LCD1602.show_string("Humidity", 0, 0)
    I2C_LCD1602.show_number(humidity, 6, 0)
    I2C_LCD1602.clear()
    I2C_LCD1602.show_string("fog", 0, 0)
    I2C_LCD1602.show_number(fog_constant, 6, 0)
    I2C_LCD1602.clear()
loops.every_interval(60000, on_every_interval)

def on_every_interval2():
    global fog_constant
    # requesting info from DHT22
    dht11_dht22.query_data(DHTtype.DHT11, DigitalPin.P0, True, False, True)
    # fog detection
    if humidity >= 90 or Tc <= 10:
        max7219_matrix.brightness_all(15)
        fog_constant = 1
    else:
        max7219_matrix.brightness_all(7)
        fog_constant = 0
loops.every_interval(60000, on_every_interval2)

def on_forever():
    global motion_1, motion_2, humidity, Tc, light2
    # motion sensor 1
    motion_1 = pins.digital_read_pin(DigitalPin.P1)
    # motion sensor 2
    motion_2 = pins.digital_read_pin(DigitalPin.P2)
    # DHT22 sensor humidity
    humidity = dht11_dht22.read_data(dataType.HUMIDITY)
    # DHT22 sensor temperature
    Tc = dht11_dht22.read_data(dataType.TEMPERATURE)
    # motion sensor 1
    light2 = pins.digital_read_pin(DigitalPin.P7)
basic.forever(on_forever)

# every 1 hour we check if it is night

def on_every_interval3():
    if light2 == 0:
        max7219_matrix.fill_all()
        # low brightness yet visible
        max7219_matrix.brightness_all(7)
loops.every_interval(3600000, on_every_interval3)

def on_every_interval4():
    # motion detection
    if motion_1 == 1 or motion_2 == 1:
        max7219_matrix.brightness_all(15)
    else:
        max7219_matrix.brightness_all(7)
loops.every_interval(100, on_every_interval4)
