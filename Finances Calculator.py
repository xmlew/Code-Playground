import math
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import font

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def calculate():
    #calculates time to save in years and months
    svgs = float(__savings.get())
    pr = float(__desired_item.get())
    dis = float(__disc_or_grant.get())
    years = ((pr-dis)/svgs)//12
    months = (pr-dis)/svgs
    outcome = [int(years),math.ceil(months-(years*12))]
    string_to_display = str(outcome[0]) + "Years, " + str(outcome[1]) + "Months"
    result2["text"] = string_to_display
    
    #formatting.
    if years <= 2 :
        result3["text"] = "Easy peasy!"
        result4["text"] = "Don't spend lavishly and you'll be fine :)'"
        return
    elif years < 5 and years >= 2 :
        result3["text"] = "Achievable in the mid-long term!"
        result4["text"] = "Self-discipline goes a long way!"
        return
    elif years < 25 and years >= 5 :
        result3["text"] = "Achievable in the long term!"
        result4["text"] = "Remember to plan ahead."
        return
    elif years < 70 and years >=25 :
        result3["text"] = "This may take a while."
        result4["text"] = ""
        return
    elif years >= 70 and years < 200:
        result3["text"] = "Your next generations will remember how"
        result4["text"] = "you saved this amount for them."
        return
    elif years >= 200 and years <1000:
        result3["text"] = "You sure this great great great great great"
        result4["text"] = "great great grandson/daughter is worth it?"
        return
    elif years >=1000:
        result3["text"] = "ok now you're just messing with me"
        result4["text"] = ""
        return

root = tk.Tk()
root.title("Financial Calculator")

canvas = tk.Canvas(root, height = 500, width = 450, bg = 'ivory')
canvas.pack()

frame = tk.Frame(root, bg = '#c2d4f2')
frame.place(relx=0.05,rely=0.075,relwidth=0.9, relheight=0.45)
frame2 = tk.Frame(root, bg = 'ivory')
frame2.place(relx=0.05,relwidth=0.9)
frame3 = tk.Frame(root, bg = '#c2d4f2')
frame3.place(relx = 0.05, rely = 0.55, relwidth = 0.9, relheight = 0.4)

label = tk.Label(frame2, text = "Welcome to your financial calculator!", bg = 'ivory', font =('Helvetica',18), borderwidth = 2, relief = 'ridge')
label.pack()

savtext= tk.Label(frame, text = "Please indicate your monthly savings in $ : ", bg = '#c2d4f2', font = ('Calibri', 16))
savtext.pack()
__savings = tk.Entry(frame, bg = 'white')
__savings.pack()

destext = tk.Label(frame, text = "Input the cost of your desired item in $ here: ", bg = '#c2d4f2', font = ('Calibri', 16))
destext.pack()
__desired_item = tk.Entry(frame,bg = 'white')
__desired_item.pack()

#i cant be assed to find textwrap will fix this next time lmaoborghini
grantstext = tk.Label(frame, text = "Input the monetary value of any grants, subsidies", bg = '#c2d4f2', font = ('Calibri', 14))
grantstext2 = tk.Label(frame, text = " or discounts in $ here (Put 0 if none) ", bg = '#c2d4f2', font = ('Calibri', 14))
grantstext.pack()
grantstext2.pack()
__disc_or_grant = tk.Entry(frame,bg = 'white', )
__disc_or_grant.pack()

result = tk.Label(frame3, text = "You will have to save for:",bg = '#c2d4f2', font = ('Calibri', 18))
result.pack()
result2 = tk.Label(frame3, text = "Input the values first!", bg = '#c2d4f2', font = ('Calibri', 18))
result2.pack()
result3 = tk.Label(frame3, bg = '#c2d4f2', font = ('Calibri', 16))
result3.pack()
result4 = tk.Label(frame3, bg = '#c2d4f2', font = ('Calibri', 16))
result4.pack()

button = tk.Button(frame, text = "Calculate!", font = "Calibri", bg = 'white', fg = 'black', command = calculate)
button.pack(side = 'bottom')

root.mainloop()
