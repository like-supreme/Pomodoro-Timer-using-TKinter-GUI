from tkinter import *
import time
import math as m 
# ---------------------------- CONSTANTS ------------------------------- #
# https://colorhunt.co/ color codes
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps , timer
    if timer is not None:
        window.after_cancel(timer) 
        canvas.itemconfig(timer_text , text="00:00")   
        timer_label.config(text="Timer" , fg=GREEN)
        check_marks.config(text="")
        timer = None   
    reps = 0 
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer(): 
    """for kullanmamız hataya sebebiyet verir. fonksiyon overlap olur"""  
    global reps , timer
    work_sec = WORK_MIN * 60
    rest_sec = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    if timer is not None:
        return
    reps += 1
    if reps == 8:
        timer_label.config(text="Break" , fg=PINK)
        count_down(long_break_secs)
    elif reps % 2 != 0:
        timer_label.config(text="Work"  , fg=GREEN)
        count_down(work_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Break" , fg=RED)
        count_down(rest_sec)
    else:
        timer_label.config(text="ERROR" , fg=RED)   
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = m.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text , text= f"{count_min}:{count_sec}")
    if count > 0:    
        timer = window.after(1000 , count_down , count - 1) # fonksiyon çağıracağız 1000den sonra , fonktan sonra ise count -1 yapacağız. 
    else:
        timer = None
        start_timer()
        marks = ""
        work_sessions = m.floor(reps/2)
        for _ in range(work_sessions):
            marks += CHECK_MARK
        check_marks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro ")
window.config(padx=100 , pady=50 , bg=YELLOW)
window.after(1000) # fonksiyon çağıracağız 1000den sonra , fonktan sonra ise count -1 yapacağız. 
timer_label = Label(text="Timer" , font=(FONT_NAME , 50 , "normal") , fg= GREEN , bg=YELLOW)
timer_label.grid(row=1 , column=2)
canvas = Canvas(width=200 , height=224 , bg=YELLOW , highlightthickness=0)
tomato_img = PhotoImage(file="C:/Users/mdeha/OneDrive/Masaüstü/python/day28/pomodoro_start/tomato.png")
canvas.create_image(100 , 112, image=tomato_img)
timer_text = canvas.create_text(100 , 130 , text="00:00" , fill="white" , font=(FONT_NAME , 35 , "bold"))
canvas.grid(row=2 , column=2)
st_button = Button(text="Start" , font=(FONT_NAME , 10 , "bold") , highlightthickness=0 , command=start_timer)
st_button.grid(row=3 , column=1)
rst_button = Button(text="Reset" , font=(FONT_NAME , 10 , "bold") , highlightthickness=0 , command=reset_timer)
rst_button.grid(row=3 , column=3)
check_marks = Label(fg=PINK , bg=YELLOW)
check_marks.grid(column=2 , row=4)
window.mainloop()
