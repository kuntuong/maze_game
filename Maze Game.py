import play

width = play.screen.width / 2
height = play.screen.height / 2

border_top = height
border_bottom = height * -1
border_right = width 
border_left = width * -1
#words is what to be displayed
#x and y is the coordinates
#Font is to be chosen to display what type of font
text = play.new_text(
        words='<-    Image      ->',
        x=-60,
        y=0,
        font=None,
        font_size=40
    )

#color is the color of the circle
#x and y is the coordinates
#radius is how big the circl eis
#border_color is the color of the circle's border
cir = play.new_circle(
        color='green',
        x=-240,
        y=-0,
        radius=10,
        border_color='light green'
    )

wall_1 = play.new_box(
        color = "black",
        x = 0,
        y = 0,
        width = 100,
        height = 10
    )

wall_2 = play.new_box(
        color = "black",
        x = -50,
        y = -25,
        width = 10,
        height = 60
    )

wall_3 = play.new_box(
        color = "black",
        x = -120,
        y = -60,
        width = 150,
        height = 10
    )

wall_4 = play.new_box(
        color = "black",
        x = -220,
        y = 5,
        width = 140,
        height = 10
    )

wall_5 = play.new_box(
        color = "black",
        x = -290,
        y = 85,
        width = 10,
        height = 170
    )

wall_6 = play.new_box(
        color = "black",
        x = -90,
        y = 90,
        width = 140,
        height = 10
    )

finish = play.new_text(
        words="Finish!",
        x=0, y=240,
        font=None,
        font_size=50
    )
#image is the link for the image
#x and y are the coordinates
#size is the size of the image
# pic = play.new_image(
#         image='risky-assumptions.jpeg',
#         x=190,
#         y=0,
#         size=30
#     )

@play.when_program_starts
def start():
    text.hide()
    # pic.hide()
    cir.start_physics(bounciness=0.2)
    wall_1.start_physics(can_move=False)
    wall_2.start_physics(can_move=False)
    wall_3.start_physics(can_move=False)
    wall_4.start_physics(can_move=False)
    wall_5.start_physics(can_move=False)
    wall_6.start_physics(can_move=False)
    
    #pass

@play.repeat_forever
def stay():
    cir.physics.y_speed = 0
    cir.physics.x_speed = 0

    if play.key_is_pressed('up'):
        # cir.y = cir.y + 5
        cir.physics.y_speed = 10
    if play.key_is_pressed('down'):
        # cir.y = cir.y - 5
        cir.physics.y_speed = -10
    if play.key_is_pressed('right'):
        # cir.x = cir.x + 5
        cir.physics.x_speed = 10
    if play.key_is_pressed('left'):
        # cir.x = cir.x - 5
        cir.physics.x_speed = -10

    if cir.is_touching(finish):
        wall_1.hide()
        wall_2.hide()
        wall_3.hide()
        wall_4.hide()
        wall_5.hide()
        wall_6.hide()
        finish.hide()

        play.new_text(words="CøNG®ATULATIøNß! You have won!", x=0, y=0, font=None, font_size=60
        , color="blue")

#or use (more accurate but lags more when played)

# @play.when_key_pressed('up')
# async def do(key):
#     cir.y = cir.y + 5
# @play.when_key_pressed('down')
# async def do(key):
#     cir.y = cir.y - 5
# @play.when_key_pressed('right')
# async def do(key):
#     cir.x = cir.x + 5
# @play.when_key_pressed('left')
# async def do(key):
#     cir.x = cir.x - 5

    if cir.y > border_top:
        cir.y = cir.y - 5
    if cir.y < border_bottom:
        cir.y = cir.y + 5
    if cir.x > border_right:
        cir.x = cir.x - 5
    if cir.x < border_left:
        cir.x = cir.x + 5

    
play.start_program()