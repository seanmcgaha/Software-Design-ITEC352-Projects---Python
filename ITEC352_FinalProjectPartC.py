#Sean McGaha Final Project Part B
#Travel Booking Form

import tkinter as tk
from tkinter import ttk, messagebox


#Function to write form data to a file
def save_data_to_file(name, email, phone, destination, travel_date, travelers, insurance):
    """Writes form data to a file."""
    with open("Travel_booking.txt", "a") as file: #changed file extension to .txt for variety
        file.write(f"{name},{email},{phone},{destination},{travel_date},{travelers},{insurance}\n")

def save_data():
    """Collects form data and calls the save_data_to_file function"""
    #Collects user input
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    destination = destination_combobox.get()
    travel_date = travel_date_entry.get()
    travelers = num_travelers_spinbox.get()
    insurance = insurance_var.get()

    if not name or not email or not phone:
        messagebox.showwarning("Input error", "Name, Email, and Phone are required fields!")
        return
    
    #Save data to file
    save_data_to_file(name, email, phone, destination, travel_date, travelers, insurance)

    

    #Confirmation message
    messagebox.showinfo("Success", "Booking details saved successfully!")

    #clear the form fields
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    travel_date_entry.delete(0, tk.END)
    destination_combobox.set("")
    num_travelers_spinbox.delete(0, tk.END)
    num_travelers_spinbox.insert(0, "1")
    insurance_var.set("No")


#main window
window = tk.Tk()
window.title("McGaha Travel Booking Form")

frame = tk.Frame(window)
frame.pack(padx=20, pady=20)

#Personal Information Frame
personal_info_frame = tk.LabelFrame(frame, text="Personal Information")
personal_info_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

name_label = tk.Label(personal_info_frame, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(personal_info_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

email_label = tk.Label(personal_info_frame, text="Email:")
email_label.grid(row=1, column=0, padx=5, pady=5)
email_entry = tk.Entry(personal_info_frame)
email_entry.grid(row=1, column=1, padx=5, pady=5)

phone_label = tk.Label(personal_info_frame, text="Phone:")
phone_label.grid(row=2, column=0, padx=5, pady=5)
phone_entry = tk.Entry(personal_info_frame)
phone_entry.grid(row=2, column=1, padx=5, pady=5)


#travel details frame
travel_details_frame = tk.LabelFrame(frame, text="Travel Details")
travel_details_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

destination_label = tk.Label(travel_details_frame, text="Destination:")
destination_label.grid(row=0, column=0, padx=5, pady=5)
destination_combobox = ttk.Combobox(travel_details_frame, values=["Europe", "Asia", "Americas", "Africa", "Australia"])
destination_combobox.grid(row=0, column=1, padx=5, pady=5)

travel_date_label = tk.Label(travel_details_frame, text="Travel Date:")
travel_date_label.grid(row=1, column=0, padx=5, pady=5)
travel_date_entry = tk.Entry(travel_details_frame)
travel_date_entry.grid(row=1, column=1, padx=5, pady=5)

num_travelers_label = tk.Label(travel_details_frame, text="Number of Travelers:")
num_travelers_label.grid(row=2, column=0, padx=5, pady=5)
num_travelers_spinbox = tk.Spinbox(travel_details_frame, from_=1, to=20)
num_travelers_spinbox.grid(row=2, column=1, padx=5, pady=5)

#Additional Options Frame
options_frame = tk.Label(frame, text="Additional Options")
options_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

insurance_var = tk.StringVar(value="No")
insurance_checkbox = tk.Checkbutton(options_frame, text="Include Travel Insurance", variable=insurance_var, onvalue="Yes", offvalue="No")
insurance_checkbox.grid(row=0, column=0, padx=5, pady=5)

#Save Button
save_button = tk.Button(frame, text="Save Booking", command=save_data)
save_button.grid(row=3, column=0, padx=10, pady=10)

window.mainloop()