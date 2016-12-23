from tkinter import *

window = Tk()
window.title('Rating Text Generator')
window.resizable(width=False, height=False)

def ratingtext():
    ex1 = entry1_0.get()
    ex2 = entry2_0.get()
    ex3 = entry3_0.get()
    ex4 = entry4_0.get()
    ex5 = entry5_0.get()
    if ex1 != "":
        d11 = entry1_1.get()
        category1 = "~" + ex1 + "<br><b>" + d11 + "<b>"
    if ex2 != "":
        d21 = entry2_1.get()
        category1 = category1 + "<br><br>" + ex2 + "<br><b>" + d21 + "<b>"
    if ex3 != "":
        d31 = entry3_1.get()
        category1 = category1 + "<br><br>" + ex3 + "<br><b>" + d31 + "<b>"
    if ex4 != "":
        d41 = entry4_1.get()
        category1 = category1 + "<br><br>" + ex4 + "<br><b>" + d41 + "<b>"
    if ex5 != "":
        d51 = entry5_1.get()
        category1 = category1 + "<br><br>" + ex5 + "<br><b>" + d51 + "<b>"

    if ex1 != "":
        d12 = entry1_2.get()
        category2 = "~" + ex1 + "<br><b>" + d12 + "<b>"
    if ex2 != "":
        d22 = entry2_2.get()
        category2 = category2 + "<br><br>" + ex2 + "<br><b>" + d22 + "<b>"
    if ex3 != "":
        d32 = entry3_2.get()
        category2 = category2 + "<br><br>" + ex3 + "<br><b>" + d32 + "<b>"
    if ex4 != "":
        d42 = entry4_2.get()
        category2 = category2 + "<br><br>" + ex4 + "<br><b>" + d42 + "<b>"
    if ex5 != "":
        d52 = entry5_2.get()
        category2 = category2 + "<br><br>" + ex5 + "<br><b>" + d52 + "<b>"

    if ex1 != "":
        d13 = entry1_3.get()
        category3 = "~" + ex1 + "<br><b>" + d13 + "<b>"
    if ex2 != "":
        d23 = entry2_3.get()
        category3 = category3 + "<br><br>" + ex2 + "<br><b>" + d23 + "<b>"
    if ex3 != "":
        d33 = entry3_3.get()
        category3 = category3 + "<br><br>" + ex3 + "<br><b>" + d33 + "<b>"
    if ex4 != "":
        d43 = entry4_3.get()
        category3 = category3 + "<br><br>" + ex4 + "<br><b>" + d43 + "<b>"
    if ex5 != "":
        d53 = entry5_3.get()
        category3 = category3 + "<br><br>" + ex5 + "<br><b>" + d53 + "<b>"

    if ex1 != "":
        d14 = entry1_4.get()
        category4 = "~" + ex1 + "<br><b>" + d14 + "<b>"
    if ex2 != "":
        d24 = entry2_4.get()
        category4 = category4 + "<br><br>" + ex2 + "<br><b>" + d24 + "<b>"
    if ex3 != "":
        d34 = entry3_4.get()
        category4 = category4 + "<br><br>" + ex3 + "<br><b>" + d34 + "<b>"
    if ex4 != "":
        d44 = entry4_4.get()
        category4 = category4 + "<br><br>" + ex4 + "<br><b>" + d44 + "<b>"
    if ex5 != "":
        d54 = entry5_4.get()
        category4 = category4 + "<br><br>" + ex5 + "<br><b>" + d54 + "<b>"

    if ex1 != "":
        d15 = entry1_5.get()
        category5 = "~" + ex1 + "<br><b>" + d15 + "<b>"
    if ex2 != "":
        d25 = entry2_5.get()
        category5 = category5 + "<br><br>" + ex2 + "<br><b>" + d25 + "<b>"
    if ex3 != "":
        d35 = entry3_5.get()
        category5 = category5 + "<br><br>" + ex3 + "<br><b>" + d35 + "<b>"
    if ex4 != "":
        d45 = entry4_5.get()
        category5 = category5 + "<br><br>" + ex4 + "<br><b>" + d45 + "<b>"
    if ex5 != "":
        d55 = entry5_5.get()
        category5 = category5 + "<br><br>" + ex5 + "<br><b>" + d55 + "<b>"
    if ex1 != "":
        output_var.set("Your ratingTxt has been created. You can now Paste it where needed.")
    else:
        output_var.set("No text entered into 1st category.")

    print("\"ratingTxt\":\"-~NA" + category1 + category2 + category3 + category4 + category5 + "\",")
    entry_output.insert(0,"\"ratingTxt\":\"-~NA" + category1 + category2 + category3 + category4 + category5 + "\",")

def cleartext():
    entry1_0.delete(0, END)
    entry1_1.delete(0, END)
    entry1_2.delete(0, END)
    entry1_3.delete(0, END)
    entry1_4.delete(0, END)
    entry1_5.delete(0, END)
    entry2_0.delete(0, END)
    entry2_1.delete(0, END)
    entry2_2.delete(0, END)
    entry2_3.delete(0, END)
    entry2_4.delete(0, END)
    entry2_5.delete(0, END)
    entry3_0.delete(0, END)
    entry3_1.delete(0, END)
    entry3_2.delete(0, END)
    entry3_3.delete(0, END)
    entry3_4.delete(0, END)
    entry3_5.delete(0, END)
    entry4_0.delete(0, END)
    entry4_1.delete(0, END)
    entry4_2.delete(0, END)
    entry4_3.delete(0, END)
    entry4_4.delete(0, END)
    entry4_5.delete(0, END)
    entry5_0.delete(0, END)
    entry5_1.delete(0, END)
    entry5_2.delete(0, END)
    entry5_3.delete(0, END)
    entry5_4.delete(0, END)
    entry5_5.delete(0, END)

program_Label = Label(window, text="Rating Text Generator")
print_Btn = Button(window, text="Print", fg="white", bg="green", width=10, overrelief=SUNKEN, command=ratingtext)
clear_Btn = Button(window, text="Erase", fg="red", width=10, overrelief=SUNKEN, command=cleartext)

rating0_Label = Label(window, text="Category Name")
rating1_Label = Label(window, text="1")
rating2_Label = Label(window, text="2")
rating3_Label = Label(window, text="3")
rating4_Label = Label(window, text="4")
rating5_Label = Label(window, text="5")

entry1_0 = Entry(window)
entry1_1 = Entry(window)
entry1_2 = Entry(window)
entry1_3 = Entry(window)
entry1_4 = Entry(window)
entry1_5 = Entry(window)

entry2_0 = Entry(window)
entry2_1 = Entry(window)
entry2_2 = Entry(window)
entry2_3 = Entry(window)
entry2_4 = Entry(window)
entry2_5 = Entry(window)

entry3_0 = Entry(window)
entry3_1 = Entry(window)
entry3_2 = Entry(window)
entry3_3 = Entry(window)
entry3_4 = Entry(window)
entry3_5 = Entry(window)

entry4_0 = Entry(window)
entry4_1 = Entry(window)
entry4_2 = Entry(window)
entry4_3 = Entry(window)
entry4_4 = Entry(window)
entry4_5 = Entry(window)

entry5_0 = Entry(window)
entry5_1 = Entry(window)
entry5_2 = Entry(window)
entry5_3 = Entry(window)
entry5_4 = Entry(window)
entry5_5 = Entry(window)

entry_output = Entry(window, width=125)

program_Label.grid(row=0, columnspan=6, sticky=N)
clear_Btn.grid(row=1, column=0, sticky=N)
print_Btn.grid(row=1, column=5, sticky=N)


rating0_Label.grid(row=2, column=0)
rating1_Label.grid(row=2, column=1)
rating2_Label.grid(row=2, column=2)
rating3_Label.grid(row=2, column=3)
rating4_Label.grid(row=2, column=4)
rating5_Label.grid(row=2, column=5)

entry1_0.grid(row=3, column=0)
entry1_1.grid(row=3, column=1)
entry1_2.grid(row=3, column=2)
entry1_3.grid(row=3, column=3)
entry1_4.grid(row=3, column=4)
entry1_5.grid(row=3, column=5)

entry2_0.grid(row=4, column=0)
entry2_1.grid(row=4, column=1)
entry2_2.grid(row=4, column=2)
entry2_3.grid(row=4, column=3)
entry2_4.grid(row=4, column=4)
entry2_5.grid(row=4, column=5)

entry3_0.grid(row=5, column=0)
entry3_1.grid(row=5, column=1)
entry3_2.grid(row=5, column=2)
entry3_3.grid(row=5, column=3)
entry3_4.grid(row=5, column=4)
entry3_5.grid(row=5, column=5)

entry4_0.grid(row=6, column=0)
entry4_1.grid(row=6, column=1)
entry4_2.grid(row=6, column=2)
entry4_3.grid(row=6, column=3)
entry4_4.grid(row=6, column=4)
entry4_5.grid(row=6, column=5)

entry5_0.grid(row=7, column=0)
entry5_1.grid(row=7, column=1)
entry5_2.grid(row=7, column=2)
entry5_3.grid(row=7, column=3)
entry5_4.grid(row=7, column=4)
entry5_5.grid(row=7, column=5)

output_var = StringVar()
output_var.set("Press 'Print' for an output.")
output = Label(textvariable=output_var)
output.grid(row=8, columnspan=6, sticky=W)

entry_output.grid(row=9, column=0, columnspan=6, sticky=W)
eval1 = "test"
window.mainloop()