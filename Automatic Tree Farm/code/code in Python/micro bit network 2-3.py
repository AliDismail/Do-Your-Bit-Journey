# micro bit 3

def on_received_number(receivedNumber):
    if receivedNumber == 0:
        servos.P0.set_angle(180)
        servos.P1.set_angle(180)
        servos.P2.set_angle(180)
    elif receivedNumber == 1:
        servos.P0.set_angle(-180)
        servos.P1.set_angle(-180)
        servos.P2.set_angle(-180)
radio.on_received_number(on_received_number)

# micro bit 2

def on_button_pressed_a():
    radio.send_number(0)
input.on_button_pressed(Button.A, on_button_pressed_a)

# micro bit 2

def on_button_pressed_b():
    radio.send_number(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(10)