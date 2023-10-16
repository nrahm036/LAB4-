#Copy+pasted from THONY

#Define colour states
import time

# Define the states of the traffic light
RED = 0
GREEN = 1
YELLOW = 2

# Initialize the initial state
current_state = RED

# Define the maximum number of cars that can trigger a transition
max_cars = 5

#ensure opposite light isnt green at the same time as current light
opposite_light_is_green = False

while True:
    # Check the current state 
    if current_state == GREEN:
        time.sleep(5)  
        if cars <= max_cars:
            current_state = GREEN
        else:
            current_state = YELLOW
            time.sleep(5)  
            current_state = RED

    elif current_state == RED:
        time.sleep(10)  
        if opposite_light_is_green:
            current_state = RED
        else:
            current_state = GREEN
