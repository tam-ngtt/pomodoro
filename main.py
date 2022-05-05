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
check = ""
my_timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(f"{my_timer}")
    global reps, check
    reps = 0
    checkmark.config(text="")
    timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(time_item, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_session_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Break", fg=PINK)
    else:
        count_down(work_session_sec)
        timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minute = int(count / 60)
    count_second = count % 60
    if count_second < 10:
        count_second = f"0{count_second}"
    canvas.itemconfig(time_item, text=f"{count_minute}:{count_second}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count - 1)
    else:
        # I got stuck here for some reasons. It actually works and moves to the next reps when I hit the start button.
        # However, it I want it to automatically trigger the next rep, I have to put it here
        start_timer()
        if reps % 2 == 0:
            global check
            check += "✔"
            checkmark.config(text=check)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=210, height=230, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(105, 115, image=tomato_image)
time_item = canvas.create_text(105, 140, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

# Timer label
timer = Label(text="Timer", font=(FONT_NAME, 45, "bold"), fg=GREEN, bg=YELLOW)
timer.grid(row=0, column=1)

# Start and Reset button
start_button = Button(text="Start", font=(FONT_NAME, 12), highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", font=(FONT_NAME, 12), highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

# Check mark label
checkmark = Label(font=(FONT_NAME, 18), background=YELLOW, foreground=GREEN)
checkmark.grid(row=3, column=1)
window.mainloop()
