import pygame
import time
import vgamepad as vg

pygame.init()
pygame.joystick.init()

joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("Unable to find any controller！")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"Connect to controller: {joystick.get_name()}")

gamepad = vg.VX360Gamepad()
print("Init gamepad successfully")

control_val = {
    "A": 0,
    "B": 0,
    "X": 0,
    "Y": 0,
    "LEFT_SHOULDER": 0,
    "RIGHT_SHOULDER": 0,
    "LEFT_THUMB": 0,
    "RIGHT_THUMB": 0,
    "LEFT_TRIGGER": 0.0,
    "RIGHT_TRIGGER": 0.0,
    "LEFT_JOYSTICK_X": 0.0,
    "LEFT_JOYSTICK_Y": 0.0,
    "RIGHT_JOYSTICK_X": 0.0,
    "RIGHT_JOYSTICK_Y": 0.0
}

key_map = {
    0: "A",
    1: "B",
    3: "X",
    4: "Y",
    6: "LEFT_SHOULDER",
    7: "RIGHT_SHOULDER"
}

handle_map = {
    0: "LEFT_JOYSTICK_X",
    1: "LEFT_JOYSTICK_Y",
    2: "RIGHT_JOYSTICK_X",
    3: "RIGHT_JOYSTICK_Y",
    4: "RIGHT_TRIGGER",
    5: "LEFT_TRIGGER"
}

try:
    while True:
        # Handle Controller Event
        for event in pygame.event.get():
            # Button event
            if event.type == pygame.JOYBUTTONDOWN:
                print(f"Key {event.button} Down")
                control_val[key_map[event.button]] = 1
            elif event.type == pygame.JOYBUTTONUP:
                print(f"Key {event.button} Up")
                control_val[key_map[event.button]] = 0

            # Trigger and Joystick event
            if event.type == pygame.JOYAXISMOTION:
                for axis in range(joystick.get_numaxes()):
                    axis_value = joystick.get_axis(axis)
                    print(f"Handle {axis} value: {axis_value:.2f}")
                    control_val[handle_map[axis]] = axis_value

            # Hat event
            # if event.type == pygame.JOYHATMOTION:
            #     hat_value = joystick.get_hat(event.hat)
            #     print(f"Hat {event.hat} value: {hat_value}")
            #     control_val[event.hat] = not control_val[event.hat]

        if control_val['A']:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        if control_val['B']:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        if control_val['X']:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        if control_val['Y']:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        if control_val['LEFT_SHOULDER']:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        if control_val['RIGHT_SHOULDER']:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)


        if not control_val['A']:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        if not control_val['B']:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        if not control_val['X']:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        if not control_val['Y']:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        if not control_val['LEFT_SHOULDER']:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        if not control_val['RIGHT_SHOULDER']:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)


        gamepad.left_trigger_float(value_float=control_val["LEFT_TRIGGER"])
        gamepad.right_trigger_float(value_float=control_val["RIGHT_TRIGGER"])
        gamepad.left_joystick_float(x_value_float=control_val["LEFT_JOYSTICK_X"], y_value_float=control_val["LEFT_JOYSTICK_Y"])
        gamepad.right_joystick_float(x_value_float=control_val["RIGHT_JOYSTICK_X"], y_value_float=control_val["RIGHT_JOYSTICK_Y"])

        gamepad.update()
        time.sleep(0.01)

except KeyboardInterrupt:
    print("Unexpected interrupt")
finally:
    pygame.quit()