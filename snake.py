import turtle
from random import randint

SCREEN = turtle.Screen()
single_or_multi_player = turtle.Turtle()
difficulty = turtle.Turtle()
food = turtle.Turtle()
frame = turtle.Turtle()
snake = turtle.Turtle()
mouth = turtle.Turtle()
snake_for_multi = turtle.Turtle()
mouth_for_multi = turtle.Turtle()

def settings():
    global SCREEN, player_or_players, game_difficulty, dir_x, dir_y, turn, LastTurn, turn_for_multi, LastTurn_for_multi, snake_coor, snake_coor_for_multi, dir_x_for_multi, dir_y_for_multi, what_hapend, stop, snake, single_or_multi_player, difficulty, food, frame, mouth, mouth_moves, snake_for_multi, mouth_for_multi

    SCREEN.title("Snake Game!")
    SCREEN.setup(500,150)
    SCREEN.bgcolor("black")

    player_or_players = ""
    single_or_multi_player.up()
    single_or_multi_player.goto(5,-30)
    single_or_multi_player.color("white")
    single_or_multi_player.write("press 's' for singleplayer \npress 'm' for multiplayer", align = "center", font = ("courier", 20, "bold"))
    def singleplayer():
        global player_or_players
        player_or_players = "s"
    def multiplayer():
        global player_or_players
        player_or_players = "m"
    SCREEN.onkey(singleplayer, "s")
    SCREEN.onkey(singleplayer, "S")
    SCREEN.onkey(multiplayer, "m")
    SCREEN.onkey(multiplayer, "M")
    SCREEN.listen()
    while player_or_players != "s" and player_or_players != "m":
        single_or_multi_player.ht()
    SCREEN.onkey(None, "s")
    SCREEN.onkey(None, "S")
    SCREEN.onkey(None, "m")
    SCREEN.onkey(None, "M")

    single_or_multi_player.clear()
    SCREEN.setup(700,200)

    game_difficulty = ""
    difficulty.up()
    difficulty.goto(0,-86.5)
    difficulty.color("white")
    difficulty.write("Choose the difficulty of the game:\n press 'e' for easy\n press 'n' for normal\n press 'h' for hard\n", align = "center", font = ("courier", 20, "bold"))
    def difficulty_easy():
        global game_difficulty
        game_difficulty = 150
        if player_or_players == "m":
            game_difficulty = 200
    def difficulty_normal():
        global game_difficulty
        game_difficulty = 75
        if player_or_players == "m":
            game_difficulty = 125
    def difficulty_hard():
        global game_difficulty
        game_difficulty = 0
        if player_or_players == "m":
            game_difficulty = 50
    SCREEN.onkey(difficulty_easy, "e")
    SCREEN.onkey(difficulty_easy, "E")
    SCREEN.onkey(difficulty_normal, "n")
    SCREEN.onkey(difficulty_normal, "N")
    SCREEN.onkey(difficulty_hard, "h")
    SCREEN.onkey(difficulty_hard, "H")
    SCREEN.listen()
    while game_difficulty != 150 and game_difficulty != 200 and game_difficulty != 125 and game_difficulty != 75 and game_difficulty != 50 and game_difficulty != 0:
        difficulty.ht()
    difficulty.clear()
    SCREEN.onkey(None, "e")
    SCREEN.onkey(None, "E")
    SCREEN.onkey(None, "n")
    SCREEN.onkey(None, "N")
    SCREEN.onkey(None, "h")
    SCREEN.onkey(None, "H")
    SCREEN.setup(700,700)

    food.st()
    food.up()
    food.shape("circle")
    food.shapesize(0.9)
    food.color("red")

    frame.seth(0)
    frame.ht()
    frame.speed(1000)
    frame.color("Green")
    frame.up()
    frame.goto(-310,-310)
    frame.down()
    for i in range (2):
        for i in range(31):
            frame.fd(20)
            frame.lt(90)
            frame.fd(620)
            frame.bk(620)
            frame.rt(90)
        frame.lt(90)
        for i in range(2):
            frame.fd(620)
            frame.lt(90)

    snake.st()
    snake.goto(0,0)
    snake.up()
    snake.shape("square")
    snake.color("green")
    snake.speed(10000)
    snake_coor = [(0,0)]
    stamps = []

    mouth.up()
    mouth.shape("triangle")
    mouth.color("black")
    mouth.speed(10000)
    mouth.shapesize(0.9)
    mouth_moves = 1

    if player_or_players == "m":
        snake_coor = [(100,0)]
        snake.goto(100,0)

        snake_for_multi.st()
        snake_for_multi.up()
        snake_for_multi.shape("square")
        snake_for_multi.color("green")
        snake_for_multi.speed(10000)
        snake_for_multi.goto(-100,0)

        mouth_for_multi.st()
        mouth_for_multi.up()
        mouth_for_multi.shape("triangle")
        mouth_for_multi.color("black")
        mouth_for_multi.speed(10000)
        mouth_for_multi.shapesize(0.9)

    dir_x = 0
    dir_y = 0

    turn = 0
    LastTurn = 0

    turn_for_multi = 0
    LastTurn_for_multi = 0
    snake_coor_for_multi = [(-100,0)]
    dir_x_for_multi = 0
    dir_y_for_multi = 0
    what_hapend = ""

    stop = False

settings()

def getRandPos(): 
    return ((randint(-15,15)*20,randint(-15,15)*20))

def actualiseDisplay():
    global mouth_moves
    tracer = SCREEN.tracer()
    SCREEN.tracer(0)
    snake.clearstamps(len(snake_coor))
    if player_or_players == "m":
        snake_for_multi.clearstamps(len(snake_coor_for_multi))
    food.goto(food_coor[0],food_coor[1])

    for x,y in snake_coor:
        snake.goto(x,y)
        snake.stamp()
    if player_or_players == "m":
        for x,y in snake_coor_for_multi:
            snake_for_multi.goto(x,y)
            snake_for_multi.stamp()
    SCREEN.tracer(tracer)

    x,y = snake_coor[0]
    mx,my = snake_coor_for_multi[0]

    if player_or_players == "m":
        if turn == 1:
            mouth.seth(180)
            mouth.goto(x+3,y)

        if turn_for_multi == 1:
            mouth_for_multi.seth(180)
            mouth_for_multi.goto(mx+3,my)

        if turn == 2:
            mouth.seth(0)
            mouth.goto(x-3,y)

        if turn_for_multi == 2:
            mouth_for_multi.seth(0)
            mouth_for_multi.goto(mx-3,my)

        if turn == 3:
            mouth.seth(270)
            mouth.goto(x,y+3)

        if turn_for_multi == 3:
            mouth_for_multi.seth(270)
            mouth_for_multi.goto(mx,my+3)

        if turn == 4:
            mouth.seth(90)
            mouth.goto(x,y-3)

        if turn_for_multi == 4:
            mouth_for_multi.seth(90)
            mouth_for_multi.goto(mx,my-3)

    if player_or_players == "s" and turn == 1 and mouth_moves == 1:
        mouth.goto(x+6,y)
        mouth.seth(180)
        SCREEN.ontimer(mouth.shapesize(0.5),60)
        mouth_moves = 2
    if player_or_players == "s" and turn == 1 and mouth_moves == 2:
        mouth.goto(x+3,y)
        SCREEN.ontimer(mouth.shapesize(0.9),40)
        mouth_moves = 1

    if player_or_players == "s" and turn == 2 and mouth_moves == 1:
        mouth.goto(x-6,y)
        mouth.seth(0)
        SCREEN.ontimer(mouth.shapesize(0.5),60)
        mouth_moves = 2
    if player_or_players == "s" and turn == 2 and mouth_moves == 2:
        mouth.goto(x-3,y)
        SCREEN.ontimer(mouth.shapesize(0.9),40)
        mouth_moves = 1

    if player_or_players == "s" and turn == 3 and mouth_moves == 1:
        mouth.goto(x,y+6)
        mouth.seth(270)        
        SCREEN.ontimer(mouth.shapesize(0.5),60)
        mouth_moves = 2
    if player_or_players == "s" and turn == 3 and mouth_moves == 2:
        mouth.goto(x,y+3)
        SCREEN.ontimer(mouth.shapesize(0.9),40)
        mouth_moves = 1

    if player_or_players == "s" and turn == 4 and mouth_moves == 1:
        mouth.goto(x,y-6)
        mouth.seth(90)
        SCREEN.ontimer(mouth.shapesize(0.5),60)
        mouth_moves = 2
    if player_or_players == "s" and turn == 4 and mouth_moves == 2:
        mouth.goto(x,y-3)
        SCREEN.ontimer(mouth.shapesize(0.9),40)
        mouth_moves = 1

def isSnakeAbove(random):
    global snake_coor, snake_coor_for_multi
    times = 0
    random = random

    while times < len(snake_coor):
        while random == snake_coor[times]:
            random = ((randint(-15,15)*20,randint(-15,15)*20))
        times = times + 1

    if player_or_players == "m":
        times = 0
        while times < len(snake_coor_for_multi):
            while random == snake_coor_for_multi[times]:
                random = ((randint(-15,15)*20,randint(-15,15)*20))
            times = times + 1

    return random

food_coor = isSnakeAbove(getRandPos())

def actualisePos():
    global snake_coor, snake_coor_for_multi, food_coor, stop
    avance()

    if isSelfCollision() or isBorderCollision() or isSnakesCollision_for_multi():
        stop = True

    if isFoodCollision():
        append()
        food_coor = isSnakeAbove(getRandPos())

    if isFoodCollision_for_multi():
        append_for_multi()
        food_coor = isSnakeAbove(getRandPos())

def loop():
    if stop:
        gameOver()
        return

    actualisePos()
    actualiseDisplay()
    SCREEN.ontimer(loop,game_difficulty)

def isSelfCollision():
    global snake_coor, LastTurn, turn, snake_coor_for_multi, LastTurn_for_multi, turn_for_multi, what_hapend

    if len(snake_coor) >= 2 or len(set(snake_coor)) < len(snake_coor):
        if LastTurn == 1 and turn == 2 or LastTurn == 2 and turn == 1 or LastTurn == 3 and turn == 4  or LastTurn == 4 and turn == 3 or len(set(snake_coor)) < len(snake_coor):
            what_hapend = "   right ate himself\n- left is the winner -"
            return True

    if len(snake_coor_for_multi) >= 2 or len(set(snake_coor_for_multi)) < len(snake_coor_for_multi):
        if LastTurn_for_multi == 1 and turn_for_multi == 2 or LastTurn_for_multi == 2 and turn_for_multi == 1 or LastTurn_for_multi == 3 and turn_for_multi == 4  or LastTurn_for_multi == 4 and turn_for_multi == 3 or len(set(snake_coor_for_multi)) < len(snake_coor_for_multi):
            what_hapend = "   left ate himself\n- right is the winner -"
            return True

def isFoodCollision():
    sx,sy = snake_coor[0]
    fx,fy = food_coor
    if sx >= fx - 10 and sx <= fx + 10 and sy >= fy - 10 and sy <= fy + 10:
        return True

def isFoodCollision_for_multi():
    smx,smy = snake_coor_for_multi[0]
    fx,fy = food_coor
    if smx >= fx - 10 and smx <= fx + 10 and smy >= fy - 10 and smy <= fy + 10:
        return True

def isBorderCollision():
    global what_hapend
    x,y = snake_coor[0]

    if -310 > x or  x > 310 or -310 > y or y > 310:
        what_hapend = "right got out of the border\n   - left is the winner -"
        return True

    x,y = snake_coor_for_multi[0]
    if -310 > x or  x > 310 or -310 > y or y > 310:
        what_hapend = "left got out of the border\n  - right is the winner -"
        return True

def isSnakesCollision_for_multi():
    global snake_coor, snake_coor_for_multi, what_hapend
    times = 0

    while times < len(snake_coor_for_multi) and player_or_players == "m":
        if snake_coor[0] == snake_coor_for_multi[times]:
            if snake_coor[0] == snake_coor_for_multi[0]:
                what_hapend = "you ate each other\n    - draw -"
                return True
            what_hapend = "     right ate left\n- left is the winner -"
            return True
        times = times + 1

    times = 0
    while times < len(snake_coor) and player_or_players == "m":
        if snake_coor_for_multi[0] == snake_coor[times]:
            what_hapend = "left ate right\n- right is the winner -"
            return True
        times = times + 1

def avance():
    global snake_coor, snake_coor_for_multi

    x, y = snake_coor[0]
    x += dir_x*20
    y += dir_y*20
    snake_coor.insert(0, (x, y))
    snake_coor.pop(-1)

    if player_or_players == "m":
        x, y = snake_coor_for_multi[0]
        x += dir_x_for_multi*20
        y += dir_y_for_multi*20
        snake_coor_for_multi.insert(0, (x, y))
        snake_coor_for_multi.pop(-1)    

def append():
    global snake_coor
    a = snake_coor[-1][:]
    snake_coor.append(a)

def append_for_multi():
    global snake_coor_for_multi
    a = snake_coor_for_multi[-1][:]
    snake_coor_for_multi.append(a)

def setDir(x,y):
    global dir_x, dir_y
    dir_x = x
    dir_y = y

def setDir_for_multi(x,y):
    global dir_x_for_multi, dir_y_for_multi
    dir_x_for_multi = x
    dir_y_for_multi = y

def right():
    global LasutTurn, turn
    LasutTurn = turn
    turn = 1
    setDir(1,0)

def left():
    global LasutTurn, turn
    LasutTurn = turn
    turn = 2
    setDir(-1,0)

def up():
    global LasutTurn, turn
    LasutTurn = turn
    turn = 3
    setDir(0,1)

def down():
    global LasutTurn, turn
    LasutTurn = turn
    turn = 4
    setDir(0,-1)   

def D_right():
    global LastTurn_for_multi, turn_for_multi
    LastTurn_for_multi = turn_for_multi
    turn_for_multi = 1
    setDir_for_multi(1,0)

def A_left():
    global LastTurn_for_multi, turn_for_multi
    LastTurn_for_multi = turn_for_multi
    turn_for_multi = 2
    setDir_for_multi(-1,0)

def W_up():
    global LastTurn_for_multi, turn_for_multi
    LastTurn_for_multi = turn_for_multi
    turn_for_multi = 3
    setDir_for_multi(0,1)

def S_down():
    global LastTurn_for_multi, turn_for_multi
    LastTurn_for_multi = turn_for_multi
    turn_for_multi = 4
    setDir_for_multi(0,-1)

def reset_settings():
    global d 
    d.clear()
    SCREEN.onclick(None)
    SCREEN.onkey(None, "r")  
    SCREEN.onkey(None, "R")
    settings()
    SCREEN.onkey(up, "Up")
    SCREEN.onkey(down, "Down")
    SCREEN.onkey(right, "Right")
    SCREEN.onkey(left, "Left")
    if player_or_players == "m":
        SCREEN.onkey(W_up, "w")
        SCREEN.onkey(W_up, "w")
        SCREEN.onkey(S_down, "s")
        SCREEN.onkey(S_down, "S")
        SCREEN.onkey(D_right, "d")
        SCREEN.onkey(D_right, "D")
        SCREEN.onkey(A_left, "a")
        SCREEN.onkey(A_left, "A")
    SCREEN.listen()
    loop()
    turtle.mainloop()  

def gameOver():
    global d
    d = turtle.Turtle()
    d.up()
    d.ht()
    d.color("red")
    snake.ht()
    snake.clearstamps(len(snake_coor))
    food.ht()
    frame.clear()
    mouth_for_multi.ht()

    if player_or_players == "s":
        SCREEN.setup(600 , 250)
        d.goto(0,60)
        d.write("GAME OVER", align = "center", font = ("courier", 30, "bold"))
        d.goto(0,25)
        d.color("white")
        G_O = "Score: "+str(len(snake_coor)-1)
        d.write(G_O, align = "center", font = ("courier", 20, "bold"))

        d.goto(0,-90)
        d.color("blue")
        d.write("   press 'r' to restart the game\nclick on the game screen to close", align = "center", font = ("courier", 20, "bold"))
        SCREEN.onkey(reset_settings, "r")
        SCREEN.onkey(reset_settings, "R")
        SCREEN.onclick(lambda*a:[SCREEN.bye(),exit()])
        SCREEN.listen()

    if player_or_players == "m":
        snake_for_multi.ht()
        snake_for_multi.clearstamps(len(snake_coor))
        SCREEN.setup(600 , 300)
        d.goto(0,100)
        d.write("GAME OVER", align = "center", font = ("courier", 30, "bold"))

        d.goto(0,40)
        d.write(what_hapend, align = "center", font = ("courier", 20, "bold"))

        d.goto(0,-10)
        d.color("white")
        score = "Left Player Score: "+str(len(snake_coor_for_multi)-1)
        d.write(score, align = "center", font = ("courier", 20, "bold"))

        d.goto(0,-35)
        score = "Right Player Score: "+str(len(snake_coor)-1)
        d.write(score, align = "center", font = ("courier", 20, "bold"))

        d.goto(0,-130)
        d.color("blue")
        d.write("   press 'r' to restart the game\nclick on the game screen to close", align = "center", font = ("courier", 20, "bold"))
        SCREEN.onkey(reset_settings, "r")
        SCREEN.onkey(reset_settings, "R")
        SCREEN.onclick(lambda*a:[SCREEN.bye(),exit()])
        SCREEN.listen()

SCREEN.onkey(up, "Up")
SCREEN.onkey(down, "Down")
SCREEN.onkey(right, "Right")
SCREEN.onkey(left, "Left")
if player_or_players == "m":
    SCREEN.onkey(W_up, "w")
    SCREEN.onkey(W_up, "w")
    SCREEN.onkey(S_down, "s")
    SCREEN.onkey(S_down, "S")
    SCREEN.onkey(D_right, "d")
    SCREEN.onkey(D_right, "D")
    SCREEN.onkey(A_left, "a")
    SCREEN.onkey(A_left, "A")
SCREEN.listen()
loop()
turtle.mainloop()
