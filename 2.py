import tkinter as tk
from tkinter import messagebox

class AddressBook:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Address Book")
        self.contacts = []
        self.name = tk.StringVar()
        self.phone = tk.StringVar()
        self.address = tk.StringVar()
        self.name_label = tk.Label(self.window, text="Name:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(self.window, textvariable=self.name)
        self.name_entry.grid(row=0, column=1)
        self.phone_label = tk.Label(self.window, text="Phone:")
        self.phone_label.grid(row=1, column=0)
        self.phone_entry = tk.Entry(self.window, textvariable=self.phone)
        self.phone_entry.grid(row=1, column=1)
        self.address_label = tk.Label(self.window, text="Address:")
        self.address_label.grid(row=2, column=0)
        self.address_entry = tk.Entry(self.window, textvariable=self.address)
        self.address_entry.grid(row=2, column=1)
        self.add_button = tk.Button(self.window, text="Add", command=self.add_contact)
        self.add_button.grid(row=3, column=0)
        self.view_button = tk.Button(self.window, text="View", command=self.view_contacts)
        self.view_button.grid(row=3, column=1)
        self.window.mainloop()

    def add_contact(self):
        name = self.name.get()
        phone = self.phone.get()
        address = self.address.get()
        
        if not name or not phone or not address:
            messagebox.showerror("Error", "Please fill in all fields")
            return
        
        for contact in self.contacts:
            if contact["name"] == name and contact["phone"] == phone and contact["address"] == address:
                messagebox.showerror("Error", "Contact already exists")
                return
        
        self.contacts.append({"name": name, "phone": phone, "address": address})
        self.name.set("")
        self.phone.set("")
        self.address.set("")
        messagebox.showinfo("Success", "Contact added successfully")

    def view_contacts(self):
        contact_list = tk.Tk()
        contact_list.title("Contacts")
        listbox = tk.Listbox(contact_list, width=40)
        listbox.pack(padx=10, pady=10)
        
        for contact in self.contacts:
            listbox.insert(tk.END, f"Name: {contact['name']}\nPhone: {contact['phone']}\nAddress: {contact['address']}\n")
        
        contact_list.mainloop()

AddressBook()