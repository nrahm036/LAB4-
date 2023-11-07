import machine
import time
from machine import Pin
from machine import UART
#initialize UART comms Pico a to b 
uart = UART(1, 9600, tx=Pin(8), rx=Pin(9))
uart.init(9600, bits=8, parity=None, stop=1)
#esablishes pwm output on pico a 
# p8 = machine.Pin(8)
# pwm8 = machine.PWM(p8)
# print(type(pwm8))
# # Set PWM frequency to be sent to Pico B, on pin 8
# pwm8.freq(1000) 
# #1023 = 100% so 512 = 50%
# pwm8.duty_u16(32768)                                                                   

#initialize reciever on pico b 8=tx, reciever pin
# pwm_reciever = machine.PWM(Pin(8))
expected_pwn_value = ()

print ("starting")

while True:
    uart.write('Hello')
    #(pico b) recieves pwm and processes
    if uart.any():
        recieved_message=uart.read()

        #checks if recieved_message has desired pwm value
        if recieved_message:
            print ("message =", recieved_message)

            #expected_pwm_value = float(recieved_message.split(":")[1].strip()[:-1])
            time.sleep(5)

        elif "The anolog value is" in recieved_message:
            print ("The measured pwm value was:{:.2F}%")
            uart.write("The measured pwm value was: {:.2f}%") 
            #sends response back to pico a, includes measured pwm value

        else:
            #something weird happened?
            print ("Weird, I got...", recieved_message)

            # Split the string using ":" and convert to float 
            calculated_pwm_value = (pwm_reciever.duty_u16() / 65535) * 100              
            # 65535 is the max 16 bit value, this gives percent of duty cycle
