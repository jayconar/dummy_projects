from tkinter import *
screen = Tk()
screen.title("Convert miles to kilometers")
screen.config(padx=60, pady=60)

entry = Entry()
entry.grid(column=2, row=1)
entry.insert(END, string="0")

result = Label(text="", font=("Georgia", 12))
result.grid(column=2, row=2)


def text(txt="0", position=(2, 2)):
    if position == (2, 2):
        answer = float(entry.get()) * 1.609344
        result.config(text=answer, padx=16, pady=16)
    else:
        label = Label(text=txt, font=("Georgia", 12))
        label.grid(column=position[0], row=position[1])
        label.config(padx=16, pady=16)


text("Miles", (3, 1))
text("Kilometers", (3, 2))

button = Button(text="Convert", command=text)
button.grid(column=3, row=4)
button.config(pady=12, padx=12)
mainloop()
