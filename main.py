#import all the necessary files in order to access the functions.
#Tkinter is the standard GUI library for Python.
from tkinter import *
from tkinter.messagebox import *
import math as m

# common font size.
font = ('Times New Roman',14, 'bold')

#functions to activate the working of button.
def clear():
    ex = textField.get()
    ex = ex[0:len(ex) - 1]
    textField.delete(0, END)
    textField.insert(0, ex)

#this function is created to clear of all inputs in one go.
   def all_clear():
    textField.delete(0, END)

def click_btn_function(event):
    global p
    print("btn clicked")
    b = event.widget
    text = b['text']
    print(text)

    if text = = 'x':
        textField.insert(END, "*")
        return

    if text == '=':
        try:
            ex = textField.get()
            ans = eval(ex)
            textField.delete(0, END)
            textField.insert(0, ans)
        except Exception as e:
            print("Error..", e)
            showerror("Error", e)
        return

    textField.insert(END, text)

# creating a window
window = Tk()
window.title('My Calculator')
window.geometry('300x465')

# picture label
pic = PhotoImage(file='sci.png')
headingLabel = Label(window, image=pic)
headingLabel.pack(side=TOP, pady=10)

# heading label
heading = Label(window, text='Solve your problem', font=font)
heading.pack(side=TOP)

# textfiled
textField = Entry(window, font=font, justify=CENTER)
textField.pack(side=TOP, pady=10, fill=X, padx=10)

#buttons
buttonFrame = Frame(window)
buttonFrame.pack(side=TOP, padx=10)

# adding button
temp = 1
for i in range(0, 3):
    for j in range(0, 3):
        btn = Button(buttonFrame, text=str(temp), font=font, width=5, relief='ridge', activebackground='black',
                     activeforeground='yellow')
        btn.grid(row=i, column=j)
        temp = temp + 1
        btn.bind('<Button-1>', click_btn_function)

zeroBtn = Button(buttonFrame, text='0', font=font, width=5, relief='ridge', activebackground='black',
                 activeforeground='yellow')
zeroBtn.grid(row=3, column=0)

dotBtn = Button(buttonFrame, text='.', font=font, width=5, relief='ridge', activebackground='black',
                activeforeground='yellow')
dotBtn.grid(row=3, column=1)

equalBtn = Button(buttonFrame, text='=', font=font, width=5, relief='ridge', activebackground='black',
                  activeforeground='yellow')
equalBtn.grid(row=3, column=2)

plusBtn = Button(buttonFrame, text='+', font=font, width=5, relief='ridge', activebackground='black',
                 activeforeground='yellow')
plusBtn.grid(row=0, column=3)

minusBtn = Button(buttonFrame, text='-', font=font, width=5, relief='ridge', activebackground='black',
                  activeforeground='yellow')
minusBtn.grid(row=1, column=3)

multBtn = Button(buttonFrame, text='x', font=font, width=5, relief='ridge', activebackground='black',
                 activeforeground='yellow')
multBtn.grid(row=2, column=3)

divideBtn = Button(buttonFrame, text='/', font=font, width=5, relief='ridge', activebackground='black',
                   activeforeground='yellow')
divideBtn.grid(row=3, column=3)

sqrtBtn = Button(buttonFrame, text='√', font=font, width=5, relief='ridge', activebackground='black',
                 activeforeground='yellow')
sqrtBtn.grid(row=4, column=0)

powBtn = Button(buttonFrame, text='^', font=font, width=5, relief='ridge', activebackground='black',
                activeforeground='yellow')
powBtn.grid(row=4, column=1)

factBtn = Button(buttonFrame, text='x!', font=font, width=5, relief='ridge', activebackground='black',
                 activeforeground='yellow')
factBtn.grid(row=4, column=2)

radBtn = Button(buttonFrame, text='toRad', font=font, width=5, relief='ridge', activebackground='black',
                activeforeground='yellow')
radBtn.grid(row=4, column=3)

degBtn = Button(buttonFrame, text='toDeg', font=font, width=5, relief='ridge', activebackground='black',
                activeforeground='yellow')
degBtn.grid(row=5, column=0)

sinBtn = Button(buttonFrame, text='sinθ', font=font, width=5, relief='ridge', activebackground='black',
                activeforeground='yellow')
sinBtn.grid(row=5, column=1)

cosBtn = Button(buttonFrame, text='cosθ', font=font, width=5, relief='ridge', activebackground='black',
                activeforeground='yellow')
cosBtn.grid(row=5, column=2)

tanBtn = Button(buttonFrame, text='tanθ', font=font, width=5, relief='ridge', activebackground='black',
                activeforeground='yellow')
tanBtn.grid(row=5, column=3)

clearBtn = Button(buttonFrame, text='backspace', font=font, width=11, relief='ridge', activebackground='black',
                  activeforeground='yellow', command=clear)
clearBtn.grid(row=6, column=0, columnspan=2)

allClearBtn = Button(buttonFrame, text='AC', font=font, width=11, relief='ridge', activebackground='black',
                     activeforeground='yellow', command=all_clear)
allClearBtn.grid(row=6, column=2, columnspan=2)

# binding the buttons
plusBtn.bind('<Button-1>', click_btn_function)
minusBtn.bind('<Button-1>', click_btn_function)
multBtn.bind('<Button-1>', click_btn_function)
divideBtn.bind('<Button-1>', click_btn_function)
zeroBtn.bind('<Button-1>', click_btn_function)
dotBtn.bind('<Button-1>', click_btn_function)
equalBtn.bind('<Button-1>', click_btn_function)

def enterClick(event):
    print('hi')
    e = Event()
    e.widget = equalBtn
    click_btn_function(e)

textField.bind('<Return>', enterClick)

#this function is created to calculate all the mathematical operations by calling the functions from the math library file.
 def calculate(event):
    print('btn..')
    btn = event.widget
    text = btn['text']
    print(text)
    ex = textField.get()
    answer = ''
    if text == 'toDeg':
        print("cal degree")
        answer = str(m.degrees(float(ex)))
    elif text == 'toRad':
        print('radian')
        answer = str(m.radians(float(ex)))
    elif text == 'x!':
        print("cal factorial")
        answer = str(m.factorial(int(ex)))
    elif text == 'sinθ':
        print("cal sin")
        answer = str(m.sin(m.radians(int(ex))))
    elif text == 'cosθ':
        answer = str(m.cos(m.radians(int(ex))))
    elif text == 'tanθ':
        answer = str(m.tan(m.radians(int(ex))))
    elif text == '√':
        print('sqrt')
        answer = m.sqrt(int(ex))
    elif text == '^':
        print('pow')
        base, pow = ex.split(',')
        print(base)
        print(pow)
        answer = m.pow(int(base), int(pow))
    textField.delete(0, END)
    textField.insert(0, answer)

#binding the remaining buttons
sqrtBtn.bind("<Button-1>", calculate)
powBtn.bind("<Button-1>", calculate)
factBtn.bind("<Button-1>",calculate)
radBtn.bind("<Button-1>", calculate)
degBtn.bind("<Button-1>", calculate)
sinBtn.bind("<Button-1>", calculate)
cosBtn.bind("<Button-1>", calculate)
tanBtn.bind("<Button-1>", calculate)
window.mainloop()

