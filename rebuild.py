from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
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
is_start = False


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    start_button.config(command=start_timer)
    window.after_cancel(f"{timer}")
    global reps
    reps = 0
    check_mark.config(text="")
    title.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_count, text="00:00")


# ---------------------------- STOP TIMER ------------------------------- #
def stop_timer():
    window.after_cancel(f'{timer}')
    title.config(text="Stop!", fg=RED)


# ----------------------------  PREVENT TIMER INTERVENTION  ------------------------------- #
def timer_on():
    print("Timer is on.")
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    start_button.config(command=timer_on)
    work_session = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    global reps
    reps += 1
    if reps % 8 == 0:
        title.config(text="Break", fg=RED)
        count_down(long_break)
    elif reps % 2 == 0:
        title.config(text="Break", fg=PINK)
        count_down(short_break)
    else:
        title.config(text="Work", fg=GREEN)
        count_down(work_session)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = int(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_count, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global reps
        marks = ""
        for _ in range(int(reps/2)):
            marks += "✔"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Create canvas image and timer
canvas = Canvas(width=220, height=240, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(105, 115, image=tomato_img)
timer_count = canvas.create_text(112, 140, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(row=1, column=1)


# Create timer label
title = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN, highlightthickness=0)
title.grid(row=0, column=1)

# Create start, reset button, stop button
start_button = Button(text="start", font=(FONT_NAME, 12, "bold"), highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="reset", font=(FONT_NAME, 12, "bold"), highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

stop_button = Button(text="stop", font=(FONT_NAME, 12, "bold"), highlightthickness=0, command=stop_timer)
stop_button.grid(row=2, column=1)

# Create checkmark
check_mark = Label(font=(FONT_NAME, 20), fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)


window.mainloop()