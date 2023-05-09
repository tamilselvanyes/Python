# ---------------------------- CONSTANTS ------------------------------- #
from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global timer
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="TIMER")
    check_mark.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        timer_label.config(text="WORK", fg=GREEN)
        count_down(work_sec)

    elif reps % 8 == 0:
        timer_label.config(text="LONG BREAK", fg=RED)
        count_down(long_break_sec)
    else:
        timer_label.config(text="SHORT BREAK", fg=PINK)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    global reps

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔"
            check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=100)

canvas = Canvas(width=200, height=224)

photo_image = PhotoImage(file="tomato.png")

canvas.create_image(103, 112, image=photo_image)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label()
timer_label.config(text="Timer", font=(FONT_NAME, 70))
timer_label.grid(row=0, column=1)

start_button = Button()
start_button.config(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button()
reset_button.config(text="Reset", command=reset)
reset_button.grid(row=2, column=2)

check_mark = Label()
check_mark.config(text="", fg=GREEN)
check_mark.grid(row=3, column=1)

window.mainloop()
