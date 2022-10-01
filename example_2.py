# Using Classes
from tkinter import *

class Contact_List_Window(Toplevel):
    def __init__(self, contact_information):
            super().__init__()
            self.title('All Contacts')

            for i in range(len(contact_information)):
                label = Label(self, text=contact_information[i])
                label.place(x=50, y=0 + (i*50))


class Submit_Confirmation_Window(Toplevel):
    def __init__(self):
        super().__init__()

        self.geometry('300x200')
        self.title('Contact Information Submitted!')

        confirmation_label = Label(self, text="Contact Information Submitted!")
        confirmation_label.place(x=50, y=20)


class Main_Window(Tk):
    def __init__(self, contact_information):
        super().__init__()

        label_1 = Label(self, text="Name:")
        label_2 = Label(self, text="Phone Number:")
        label_3 = Label(self, text="Address:")

        self.name_field = Entry()
        self.phone_number_field = Entry()
        self.address_field = Entry()

        label_1.place(x=50, y=50)
        self.name_field.place(x=250, y=50)

        label_2.place(x=50, y=100)
        self.phone_number_field.place(x=250, y=100)

        label_3.place(x=50, y=150)
        self.address_field.place(x=250, y=150)

        submit_button = Button(self, text="Submit", command= lambda: self.submit_contact_information(self.name_field.get(), self.phone_number_field.get(), self.address_field.get(), contact_information))
        submit_button.place(x=50, y=200)

        contact_list_button = Button(self, text="See All Contacts", command= lambda: self.open_contact_window(contact_information))
        contact_list_button.place(x=250, y=200)

        self.geometry('500x300')
        self.title('Contact Form')

    def submit_contact_information(self, name, phone_number, address, contact_information):
        individual_contact_information = [name, phone_number, address]
        contact_information.append(individual_contact_information)
        self.name_field.delete(0, 'end')
        self.phone_number_field.delete(0, 'end')
        self.address_field.delete(0, 'end')
        Submit_Confirmation_Window()
    
    def open_contact_window(self, contact_information):
        Contact_List_Window(contact_information)

if __name__ == "__main__":
    contact_information = []
    main_window = Main_Window(contact_information)
    main_window.mainloop()
