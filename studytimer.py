from tkinter import *
FONT_COLOR = "#ffe785"
BACKGROUND_COLOR = "#3c826c"
BREAK = 5
LONG_BREAK = 20
WORK = 25
REPS = 0
button_not_started = True
should_continue = True


def pop_up(window):
    window.lift()
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)


def start_countdown():
    global REPS
    global should_continue
    global button_not_started
    if button_not_started:
        should_continue = True
        button_not_started = False
        if REPS % 2 == 0 and REPS != 5:
            REPS += 1
            canvas.itemconfig(clock, text=f"TIME TO WORK!")
            window.after(3000, countdown, WORK * 60)
        elif REPS == 5:
            canvas.itemconfig(clock, text=f"TIME TO REST FOR 20 MINS!")
            window.after(3000, countdown, LONG_BREAK * 60)
            REPS = 0
        else:
            REPS += 1
            canvas.itemconfig(clock, text=f"TIME TO BREAK!")
            window.after(3000, countdown, BREAK * 60)


def countdown(seconds):
    global button_not_started
    if should_continue:
        if seconds > 0:
            canvas.itemconfig(clock, text=f"{seconds // 60}:{seconds % 60}")
            loop1 = window.after(1000, countdown, seconds - 1)
            if seconds % 60 < 10:
                window.after(0, canvas.itemconfig(clock, text=f"{seconds // 60}:0{seconds % 10}"))
            elif not should_continue:
                window.after_cancel(loop1)
                pass
        elif seconds == 0:
            canvas.itemconfig(clock, text=f"{seconds // 60}:{seconds % 60}")
            button_not_started = True
            pop_up(window)
            window.after(1000, start_countdown)


def reset():
    global REPS
    global should_continue
    global button_not_started
    should_continue = False
    button_not_started = True
    REPS = 0
    window.after(0, canvas.itemconfig(clock, text=f"00:00"))


window = Tk()
window.title("Study Timer")
window.resizable(False, False)

photo = PhotoImage(file="studyimage.png")

canvas = Canvas(bg=BACKGROUND_COLOR, width=1600, height=1200, highlightthickness=0)
canvas.create_image(800, 600, image=photo)
canvas.create_text(400, 300, text="TIMER", fill=FONT_COLOR, font=("Courier", 45, "bold"))
clock = canvas.create_text(800, 1000, text=f"00:00", fill=BACKGROUND_COLOR, font=("Courier", 60, "bold"))
canvas.pack()

start_button = Button(text="start", width=7, height=2, command=start_countdown, highlightthickness=0)
start_button.place(x=330, y=325)

reset_button = Button(text="reset", width=7, height=2, command=reset, highlightthickness=0)
reset_button.place(x=410, y=325)
window.mainloop()
