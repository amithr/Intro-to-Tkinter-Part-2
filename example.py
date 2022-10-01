from tkinter import *

# Main Window

main_window = Tk()
contact_information = []

label_1 = Label(main_window, text="Name:")
label_2 = Label(main_window, text="Phone Number:")
label_3 = Label(main_window, text="Address:")

name_field = Entry()
phone_number_field = Entry()
address_field = Entry()

label_1.place(x=50, y=50)
name_field.place(x=250, y=50)

label_2.place(x=50, y=100)
phone_number_field.place(x=250, y=100)

label_3.place(x=50, y=150)
address_field.place(x=250, y=150)

def submit_contact_form(individual_contact_information, contact_information):
    contact_information.append(individual_contact_information)
    name_field.delete(0, 'end')
    phone_number_field.delete(0, 'end')
    address_field.delete(0, 'end')

def open_submit_window(name, phone_number, address, contact_information):
    individual_contact_information = [name, phone_number, address]
    submit_window = Toplevel()
    # Routes all events in the program to this window
    # submit_window.grab_set()
    # Without geometry, window auto resizes
    submit_window.geometry('300x200')
    submit_window.title('Contact Information Submitted!')
    confirmation_label = Label(submit_window, text="Contact Information Submitted!")
    confirmation_label.place(x=50, y=20)
    submit_contact_form(individual_contact_information, contact_information)

def open_contact_window(contact_information):
    contact_window = Toplevel()
    # contact_window.grab_set()
    contact_window.title('All Contacts')
    for i in range(len(contact_information)):
        label = Label(contact_window, text=contact_information[i])
        label.place(x=50, y=0 + (i*50))


submit_button = Button(main_window, text="Submit", command= lambda: open_submit_window(name_field.get(), phone_number_field.get(), address_field.get(), contact_information))
submit_button.place(x=50, y=200)
contact_list_button = Button(main_window, text="See All Contacts", command= lambda: open_contact_window(contact_information))
contact_list_button.place(x=250, y=200)


main_window.geometry('500x300')
main_window.title('Contact Form')
main_window.mainloop()

