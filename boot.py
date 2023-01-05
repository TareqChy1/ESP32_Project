import time
from time import sleep
from machine import I2C, Pin
import ssd1306

i2c = I2C(-1, scl=Pin(22), sda=Pin(23))
oled_width = 128
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
btnA = Pin(15, Pin.IN)#Here Button A=15pin
btnB = Pin(32, Pin.IN)#Here Button B=32pin
btnC = Pin(14, Pin.IN)#Here Button C=14pin

monster_A = [
    [ 1, 0, 0, 1, 1, 0, 0, 1],
    [ 1, 0, 1, 1, 1, 1, 0, 1],
    [ 0, 1, 0, 1, 1, 0, 1, 0],
    [ 0, 1, 1, 1, 1, 1, 1, 0],
    [ 0, 1, 0, 0, 0, 0, 1, 0],
    [ 0, 0, 1, 1, 1, 1, 0, 0],
    [ 1, 1, 0, 1, 1, 0, 1, 1],
    [ 1, 0, 0, 0, 0, 0, 0, 1],
]

monster_C = [
    [ 0, 1, 0, 0, 0, 0, 1, 0],
    [ 0, 1, 1, 0, 0, 1, 1, 0],
    [ 0, 0, 1, 0, 0, 1, 0, 0],
    [ 0, 0, 0, 1, 1, 0, 0, 0],
    [ 0, 0, 1, 1, 1, 1, 0, 0],
    [ 0, 1, 0, 1, 1, 0, 1, 0],
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 0, 1, 1, 0, 0, 1, 1, 0],
]


i=1
flag = 1
ICON = monster_A
while True :
    
    logic_state_A=btnA.value()
    logic_state_B=btnB.value()
    logic_state_C=btnC.value()
    if logic_state_C == False:
        if flag == 0:
            ICON = monster_A
            flag = 1
            sleep(0.3)
        else:
            ICON = monster_C
            flag = 0
            sleep(0.3)
    oled.fill(0) # Clear the display
    if i==121:
        i=1
    for y, row in enumerate(ICON):
        for x, c in enumerate(row):
            oled.pixel(x+i, y, c)

    oled.show()
    if logic_state_A == False:
        i=int(i)+1 
        sleep(0.1)
    if logic_state_B == False:
        i=int(i)-1 
        if i == 0:
            i = 120
        sleep(0.1)  

