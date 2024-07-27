def turn_right():
    turn_left()
    turn_left()
    turn_left() 

def keep_going():
    while at_goal() != True:
        if wall_in_front() == True:
            turn_left()
        while wall_on_right() == True and wall_in_front() != True:
            move()
        while front_is_clear():
            move()
        if right_is_clear() == True and at_goal() != True:
            turn_right()
            move()
            turn_right()

keep_going()
