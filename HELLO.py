from tkinter import *

root=Tk()

root.title("Driving License")
root.geometry("400x400")

label_name = ""
label_birth = ""
label_pin = ""
label_address = ""
label_vehicle = ""

def SHOW():
    label_name['text'] = "NAME: Shreejith"
    label_birth['text'] = "DATE OF BIRTH: 2 November 2011"
    label_pin['text'] = "PIN NUMBER: 367923"
    label_address['text'] = "ADDRESS: Bethany Village, Portland, Oregon, USA"
    label_vehicle['text'] = "AUTHORISATION TO DRIVE THE FOLLOWING VEHICLE(S): Two Four"

btn = Button(root, text="Show Driving License", command=SHOW)

root.mainloop()