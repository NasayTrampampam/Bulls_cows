import tkinter as tk
from tkinter import *
import random


def do_num() -> list:
    mystery_num = []
    while len(mystery_num) < 4:
        a = random.randint(0, 9)
        if a not in mystery_num:
            mystery_num.append(a)
    return mystery_num


def move(mystery_num: list, variant: list) -> list:
    bulls = 0
    cows = 0
    counter = 0
    for number in variant:
        if number in mystery_num:
            if mystery_num[counter] == variant[counter]:
                bulls = bulls + 1
            else:
                cows = cows + 1
        counter = counter + 1
    return [bulls, cows]


def change_color(button, toggle):
    if toggle:
        button.config(fg='gray')
        button.toggle = False
    else:
        button.config(fg='#FFFFCC')
        button.toggle = True


def play_again():
    global m_n
    global moves
    global b

    # Generate a new mystery number
    m_n = do_num()

    # Clear the moves list and the number entry
    moves = []
    moves_listbox.delete(0, END)
    number_entry.delete(0, END)

    # Remove the victory message and the play again button
    moves_listbox.place_forget()

    # Add the "Try to guess the number" message and the number entry widget
    moves_listbox.place(relx=0.5, rely=0.45, anchor=CENTER)
    number_entry.place(relx=0.5, rely=0.8, anchor=CENTER)

    # Add the submit button
    check_button.place(relx=0.5, rely=0.925, anchor=CENTER)
    check_button.place_configure(relwidth=1)
    b = 0


m_n = do_num()
b = 0
moves = []

bulls_cows_window = Tk()
bulls_cows_window.title("Logic game")
bulls_cows_window.attributes("-fullscreen", True)
canvas_3 = tk.Canvas(bulls_cows_window, width=bulls_cows_window.winfo_screenwidth(),
                     height=bulls_cows_window.winfo_screenheight())
canvas_3.pack()
canvas_3.config(bg="#add8e6")

menu_image = PhotoImage(file="menu.png")
menu_image = menu_image.subsample(3, 3)
menu_button = tk.Button(bulls_cows_window, image=menu_image, bd=0, bg="#add8e6", command=bulls_cows_window.destroy)
menu_button.image = menu_image
menu_button.place(x=10, y=10)

buttons = []
for i in range(10):
    button = tk.Button(bulls_cows_window, text=str(i), width=3, height=2, font=("Arial", 20), bd=0, bg='#add8e6',
                       fg='#FFFFCC')
    button.toggle = True
    button.place(x=80 * i + 400, y=30)
    button.config(command=lambda b=button: change_color(b, b.toggle))
    buttons.append(button)

scrollbar = tk.Scrollbar(bulls_cows_window)
scrollbar.pack()

moves_listbox = Listbox(bulls_cows_window, font=("Arial", 48), width=43, yscrollcommand=scrollbar.set, height=7,
                        justify='center', bg="#add8e6", foreground="#FFFFCC", borderwidth=0,
                        highlightbackground="#add8e6")
moves_listbox.place(relx=0.5, rely=0.45, anchor=CENTER)
scrollbar.config(command=moves_listbox.yview)

number_entry = Entry(bulls_cows_window, justify='center', width=30, font=("Arial", 68), borderwidth=0, bg="#FFFFCC",
                     foreground="#add8e6")
number_entry.place(relx=0.5, rely=0.8, anchor=CENTER)

retry_img = PhotoImage(file=r"retry.png")
retry_ph = retry_img.subsample(3, 3)
play_again_button = tk.Button(bulls_cows_window, image=retry_ph, command=play_again, bd=0, bg="#add8e6")
play_again_button.place(x=80, y=200, anchor=CENTER)


def check_move():
    global moves
    global b
    num = number_entry.get()
    if len(num) != 4:
        return
    v = [int(x) for x in num]
    result = move(m_n, v)
    moves_listbox.insert(END, f"{num} - {result[0]} bulls, {result[1]} cows")
    moves.append((num, result))
    b = result[0]
    if b == 4:
        # Remove all previous moves from the listbox
        moves_listbox.delete(0, END)

        # Display the victory message
        moves_listbox.insert(END, "You win!")
        moves_listbox.place(relx=0.5, rely=0.7, anchor=CENTER)

        # Remove the number entry widget and the submit button
        number_entry.place_forget()
        check_button.place_forget()
    number_entry.delete(0, 'end')
    moves_listbox.yview(tk.END)


submit = PhotoImage(file=r"Submit.png")
check_button = Button(bulls_cows_window, text="Submit answer", image=submit, font=("Arial", 68), command=check_move,
                      borderwidth=0, bg="#FFFFCC", foreground="#add8e6")
check_button.place(relx=0.5, rely=0.925, anchor=CENTER)
check_button.place_configure(relwidth=1)

bulls_cows_window.mainloop()
