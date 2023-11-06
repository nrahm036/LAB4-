#create (write) pwm signal on Pico A
#send said signal to Pico B
#interpret signal (at pico b)
#send back (to pico a)

import machine
import time
from machine import Pin
from machine import UART

#initialize UART comms Pico a to b 
uart = UART(1, 9600, tx=Pin(8), rx=Pin(9))
uart.init(9600, bits=8, parity=None, stop=1)

#esablishes pwm output on pico a 
p8 = machine.Pin(8)
pwm8 = machine.PWM(p8)
print(type(pwm8))
# Set PWM frequency to be sent to Pico B, on pin 8
pwm8.freq(1000) 
#1023 = 100% so 512 = 50%
pwm8.duty_u16(32768)                                                                      

#initialize reciever on pico b 8=tx, reciever pin
pwm_reciever = machine.PWM(Pin(8))

#(pico a) sends pwm signal, waits 10 seconds before sending signal again
while True:
    uart.write("Duty cycle is =" + str(pwm8.duty_u16()))
    time.sleep(10)
    
    recieved_message = ""
    #(pico b) recieves pwm and processes
