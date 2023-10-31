# bounce.py
#
# Exercise 1.5
# A rubber ball is dropped from a height of 100 meters 
# and each time it hits the ground, it bounces back up to 3/5 the height it fell. 
# Write a program bounce.py that prints a table showing the height of the first 10 bounces.

def calculate_bounce(height=100, bounce_back=3/5, n_bounces=10):
    current_step, current_height = 0, height

    while current_step < n_bounces and height > 0:
        current_step += 1
        current_height = current_height * bounce_back
        print(current_step, "\t", round( current_height, 4) )
    
calculate_bounce()
    
