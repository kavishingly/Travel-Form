from tkinter import *

root = Tk()
root.minsize(644, 333)


def getVal():
    n = namevalue.get()
    ag = agevalue.get()
    gend = gendervalue.get()
    con = contactvalue.get()
    food = foodServiceValue.get()
    want_food = ""
    if food:
        want_food = "Want food"
    else:
        want_food = "Do not want food"
    f = open('Travel_form_data.txt', 'a')
    f.write(f"Name: {n},Age: {ag},Gender: {gend},Contact: {con},Food service: {want_food}\n\n")
    f.close()
    print(f"Name: {n},age: {ag},gender: {gend},contact: {con},food service: {want_food}\n\n")


Label(root, text="Welcome to Agrawal Travels - go safe, go fast", font="comicsansms 15 italic",fg="red", pady=15).grid(row=0,
                                                                                                         column=3)

name = Label(root, text="Name", pady=7)
age = Label(root, text="Age", pady=7)
gender = Label(root, text="Gender", pady=7)
contact = Label(root, text="Contact", pady=7)
name.grid(row=2, column=2)
age.grid(row=3, column=2)
gender.grid(row=4, column=2)
contact.grid(row=5, column=2)

namevalue = StringVar()
agevalue = StringVar()
gendervalue = StringVar()
contactvalue = StringVar()
foodServiceValue = IntVar()

nameentry = Entry(root, textvariable=namevalue)
ageentry = Entry(root, textvariable=agevalue)
genderentry = Entry(root, textvariable=gendervalue)
contactentry = Entry(root, textvariable=contactvalue)

nameentry.grid(row=2, column=3)
ageentry.grid(row=3, column=3)
genderentry.grid(row=4, column=3)
contactentry.grid(row=5, column=3)

# checkbox
foodService = Checkbutton(text="Want to pre-book your meal?", variable=foodServiceValue)
foodService.grid(row=6, column=3)

# submit button
Button(root, text="Submit", command=getVal).grid(row=7, column=3)

root.mainloop()
