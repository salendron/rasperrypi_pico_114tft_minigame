from LCD import LCD_1inch14, BL
from machine import Pin,PWM
import time
from scene import Scene
from clock import Clock
from events import *


if __name__=='__main__':
    pwm = PWM(Pin(BL))
    pwm.freq(1000)
    pwm.duty_u16(32768)#max 65535

    LCD = LCD_1inch14()
    main_scene = Scene(LCD, LCD.blue)
    clock = Clock(60)

    keyA = Pin(15,Pin.IN,Pin.PULL_UP)
    keyB = Pin(17,Pin.IN,Pin.PULL_UP)

    joystickUp = Pin(2 ,Pin.IN,Pin.PULL_UP)
    joystickPress = Pin(3 ,Pin.IN,Pin.PULL_UP)
    joystickLeft = Pin(16 ,Pin.IN,Pin.PULL_UP)
    joystickDown = Pin(18 ,Pin.IN,Pin.PULL_UP)
    joystickRight = Pin(20 ,Pin.IN,Pin.PULL_UP)

    event = None

    while True:
        if joystickUp.value() == 0:
            event = EVENT_UP
        elif joystickDown.value() == 0:
            event = EVENT_DOWN
        elif joystickLeft.value() == 0:
            event = EVENT_LEFT
        elif joystickRight.value() == 0:
            event = EVENT_RIGHT
        elif joystickPress.value() == 0:
            event = EVENT_PRESS
        elif keyA.value() == 0:
            event = EVENT_A
        elif keyB.value() == 0:
            event = EVENT_B
        else:
            event = None

        main_scene.process_event(event)
        main_scene.draw()
        LCD.show()
        clock.tick()

