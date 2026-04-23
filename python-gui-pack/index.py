import tkinter as tk

# Variables
students = []
student_labels = []

#functions
def addStudents():
    students.append(name_entry.get())
    
    student_label = tk.Label(window,
                font=("Arial", 16),
    text=name_entry.get()
    )

    student_label.pack(side=tk.LEFT)
    student_labels.append(student_label)

#Window Configuration
window = tk.Tk()
window.title("Student Management System") #Window title
window.geometry("700x700") #Windows Size
window.resizable(True, True)
window.configure(bg="pink")

#Components
title_label = tk.Label(window,
                text="STUDENT MANAGEMENT SYSTEM",
                font=("Arial", 24, "bold"),
                bg="pink",
                fg="black",
                padx=30,
                pady=50
            ) #1st is window 
name_label = tk.Label(window,
            text="Enter name: ",
            font=("Arial", 16, "bold"),
                bg="pink",
                fg="black",
)
name_entry = tk.Entry(window,
                width=25,
                font=("Arial", 16),
)
submit_button = tk.Button(window,
                text="Submit",
                command=addStudents
)

#Display Components
title_label.pack()
name_label.pack()
name_entry.pack(
                padx=10,
                pady=30)
submit_button.pack()

#display windows
window.mainloop()


