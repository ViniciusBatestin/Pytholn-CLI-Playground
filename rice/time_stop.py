# template for "Stopwatch: The Game"
import simplegui
# define global variables
Display = 0
successful_stop = 0
stops = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    D, t = t % 10, t // 10
    C, t = t % 10, t // 10
    B, t = t % 6, t // 6
    A, t = t % 10, t // 10

    return str(A) + ":" + str(B) + str(C) + "." + str(D)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    global stops, successful_stop
    timer.stop()
    if Display % 10 == 0:
        successful_stop += 1
    else:
        stops += 1


def reset():
    ''' Set global variable after timer.stop() to avoid concurrency bug'''
    timer.stop()
    global Display, stops, successful_stop
    Display = 0
    stops = 0
    successful_stop = 0


# define event handler for timer with 0.1 sec interval
def timer_handler():
    global Display, timer
    Display += 1
    print (str(Display))

# define draw handler
def draw(canvas):
    global Display, succesful_stop, stops
    canvas.draw_text(format(Display), (150, 200), 50, 'Green')
    canvas.draw_text(str(successful_stop) + "/" + str(stops), (10, 40), 30, 'Green')



# create frame
frame = simplegui.create_frame('Stop Watch', 400, 400)
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw)

# register event handlers
start_btn = frame.add_button('Start', start, 150)
stop_btn = frame.add_button('Stop', stop, 150)
reset_btn = frame.add_button('Reset', reset, 150)

# start frame
frame.start()
timer.start()

# Please remember to review the grading rubric
