# Implemrntation of classic arcade game Pong
# http://www.codeskulptor.org/#user38_fXasdL6Rnb_0.py

import simplegui
import random
import math

# initialize globals - pos and vel emcode Vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT/ 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in midle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left

def spawn_ball():
    global ball_pos, ball_vel 
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [random.randint(-3,3),random.randint(-3,3)]
    
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    spawn_ball()
    
def draw(c):
    global score1, score2,paddle1_pos, paddle2_pos, ball_pos, ball_vel
    

    # draw mid line and qutters
    c.draw_line([WIDTH / 2,0], [WIDTH/2, HEIGHT],1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH,HEIGHT], 1, 'White')
    c.draw_line([WIDTH - PAD_WIDTH,0], [WIDTH - PAD_WIDTH, HEIGHT], 1, 'White')

    #update ball
   
    if ball_vel[0] > 0:
        ball_vel[0] += 0.005
    else:
        ball_vel[0] -= 0.005
    if ball_vel[1] == 0:
        ball_vel[1] = 1
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] <= BALL_RADIUS or (HEIGHT - ball_pos[1]) <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    if (ball_pos[0] <= BALL_RADIUS + PAD_WIDTH and math.fabs(ball_pos[1] - paddle1_pos) < HALF_PAD_HEIGHT) or \
        (WIDTH - ball_pos[0] <= BALL_RADIUS + PAD_WIDTH and math.fabs(ball_pos[1] - paddle2_pos) < HALF_PAD_HEIGHT) :
        ball_vel[0] = -ball_vel[0]
    elif ball_pos[0] < BALL_RADIUS:
        score2 += 1
        spawn_ball()
    elif ball_pos[0] > WIDTH -BALL_RADIUS:
        score1 += 1
        spawn_ball()
        
        
    
    #draw ball
    c.draw_circle( ball_pos, BALL_RADIUS, 2 , 'White', 'White')
    #update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    if paddle1_pos >= HEIGHT-HALF_PAD_HEIGHT:
        paddle1_pos = HEIGHT-HALF_PAD_HEIGHT
    elif paddle1_pos <= HALF_PAD_HEIGHT:
        paddle1_pos = HALF_PAD_HEIGHT
        
    if paddle2_pos >= HEIGHT-HALF_PAD_HEIGHT:
        paddle2_pos = HEIGHT-HALF_PAD_HEIGHT
    elif paddle2_pos <= HALF_PAD_HEIGHT:
        paddle2_pos = HALF_PAD_HEIGHT
    #draw paddles
    c.draw_line([HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], [HALF_PAD_WIDTH,  paddle1_pos -HALF_PAD_HEIGHT],PAD_WIDTH, "White")
    c.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos+HALF_PAD_HEIGHT], [WIDTH - HALF_PAD_WIDTH, paddle2_pos-HALF_PAD_HEIGHT],PAD_WIDTH, "White")
    #draw scores
    c.draw_text(str(score1), [150, 50], 20, "White")
    c.draw_text(str(score2), [450, 50], 20, "White")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    s = 5
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel += s
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= s
    if key == simplegui.KEY_MAP["S"]:
        paddle1_vel += s
    elif key == simplegui.KEY_MAP["W"]:
        paddle1_vel-= s

           
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["down"] or key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["S"] or key == simplegui.KEY_MAP["W"]:
        paddle1_vel = 0
    
    
def button():
    new_game()
# creat frame
frame = simplegui.create_frame("Pong"  , WIDTH,  HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("New game",button)

# start frame
new_game()
frame.start()