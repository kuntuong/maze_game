import play

#defining the dimensions of the screen
width = play.screen.width / 2
height = play.screen.height / 2

#defining the top, bottom, right and left
border_top = height
border_bottom = height * -1
border_right = width 
border_left = width * -1

#the ball
cir = play.new_circle(
        color='green',
        x=-240,
        y=-0,
        radius=10,
        border_color='light green'
    )

#wall 1
wall_1 = play.new_box(
        color = "black",
        x = 0,
        y = 0,
        width = 100,
        height = 10
    )

#wall 2
wall_2 = play.new_box(
        color = "black",
        x = -50,
        y = -25,
        width = 10,
        height = 60
    )

#wall 3
wall_3 = play.new_box(
        color = "black",
        x = -120,
        y = -60,
        width = 150,
        height = 10
    )

#wall 4
wall_4 = play.new_box(
        color = "black",
        x = -220,
        y = 5,
        width = 140,
        height = 10
    )

#wall 5
wall_5 = play.new_box(
        color = "black",
        x = -290,
        y = 85,
        width = 10,
        height = 170
    )

#wall 6
wall_6 = play.new_box(
        color = "black",
        x = -90,
        y = 90,
        width = 140,
        height = 10
    )

#finish line/text
finish = play.new_text(
        words="Finish!",
        x=0, y=240,
        font=None,
        font_size=50
    )

#decorator when the program initializes
@play.when_program_starts
def start():
    #start physics for ball and all walls
    cir.start_physics(bounciness=0.2)
    wall_1.start_physics(can_move=False)
    wall_2.start_physics(can_move=False)
    wall_3.start_physics(can_move=False)
    wall_4.start_physics(can_move=False)
    wall_5.start_physics(can_move=False)
    wall_6.start_physics(can_move=False)

#decorator which will always check
@play.repeat_forever
def stay():
    #set speed of the ball
    cir.physics.y_speed = 0
    cir.physics.x_speed = 0

    #checking for any keys pressed
    if play.key_is_pressed('up'):
        cir.physics.y_speed = 10
    if play.key_is_pressed('down'):
        cir.physics.y_speed = -10
    if play.key_is_pressed('right'):
        cir.physics.x_speed = 10
    if play.key_is_pressed('left'):
        cir.physics.x_speed = -10

    #hide everything if the ball touches the finish line
    if cir.is_touching(finish):
        wall_1.hide()
        wall_2.hide()
        wall_3.hide()
        wall_4.hide()
        wall_5.hide()
        wall_6.hide()
        finish.hide()

        #congratulations text
        play.new_text(words="CøNG®ATULATIøNß! You have won!", x=0, y=0, font=None, font_size=60, color="blue")

    #collision detections
    if cir.y > border_top:
        cir.y = cir.y - 5
    if cir.y < border_bottom:
        cir.y = cir.y + 5
    if cir.x > border_right:
        cir.x = cir.x - 5
    if cir.x < border_left:
        cir.x = cir.x + 5

play.start_program()