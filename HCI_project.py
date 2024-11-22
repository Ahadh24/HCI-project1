import tkinter
import tkinter as tk
from tkinter import messagebox

root= tk.Tk()
root.title("Prime Care")



def show_medication_reminder():
    messagebox.showinfo("Medication Reminder", "Time to take your medication!")

def handle_communication():
    messagebox.showinfo("Communication","Strating a video call...")

def show_activity_suggestions():
    activity = "Today's suggestion: 30-minute walk in the park"
    messagebox.showinfo("Activity Suggestion",activity)

def show_emergency_assistance():
    messagebox.showwarning("Emergency Assistance","Emergency call activated!")

medication_button = tk.Button(root, text="Medication Reminder",command=show_medication_reminder)
medication_button.pack(pady=10)

communication_Button=tk.Button(root, text="Communication Tools", command=handle_communication)
communication_Button.pack(pady=10)

activity_Button=tk.Button(root, text="Activity Suggestions", command=show_activity_suggestions)
activity_Button.pack(pady=10)

emergency_button=tk.Button(root, text="Emergency Assistance", command=show_emergency_assistance)
emergency_button.pack(pady=10)

root.mainloop()


