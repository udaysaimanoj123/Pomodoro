import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
resps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(canva_text, text="00:00")
    label1.config(text="TIMER", fg=GREEN)
    label2.config(text="")
    global resps
    resps=0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global resps
    resps+=1

    WORK_MIN = 25*60
    SHORT_BREAK_MIN = 5*60
    LONG_BREAK_MIN = 20*60

    if resps%8==0:
        label1.config(text="L BREAK MOOD",fg=PINK)
        count_down(LONG_BREAK_MIN)
    elif resps%2==0:
        label1.config(text="BREAK MOOD",fg=RED)
        count_down(SHORT_BREAK_MIN)
    else:
        label1.config(text="WORK MOOD",fg=GREEN)
        count_down(WORK_MIN)





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    min=math.floor(count/60)
    sec=count%60
    if sec<10:
        sec=f"0{sec}"
    if min<10:
        min=f"0{min}"
    if count>0:
        canvas.itemconfig(canva_text, text=f"{min}:{sec}")
        global timer
        timer=window.after(1000, count_down, count -1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(resps/2)):
            marks+="✔"
            label2.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window=tkinter.Tk()
window.title("USM's Pomodora")
window.config(padx=100,pady=50,bg=YELLOW)


label1=tkinter.Label(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME,30,"bold"))
label1.grid(row=0,column=1)

canvas=tkinter.Canvas(width=210,height=224,bg=YELLOW,highlightthickness=0)
img=tkinter.PhotoImage(file="tomato.png")
canvas.create_image(102,112,image=img)
canva_text=canvas.create_text(100,132,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(row=1,column=1)

button1=tkinter.Button(text="Start",command=start_timer)
button1.grid(row=2,column=0)

button2=tkinter.Button(text="Reset",command=reset)
button2.grid(row=2,column=2)
label2=tkinter.Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,"bold"))
label2.grid(row=3,column=1)

window.mainloop()