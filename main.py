from tkinter import *
import time

import matplotlib.pyplot as plt




window = Tk()
window.title("Typing Speed Tester App")
window.geometry("1000x700")
window.config(bg="#1E1E2F", padx=30, pady=30)

current_index = [0]
show_text_widget = None
text_test = ""
time_up = False
start_time = 0
correct_chars = [0]

def show_text():
    global show_text_widget, text_test, time_left, time_up, start_time, correct_chars
    time_up = False
    correct_chars[0] = 0
    current_index[0] = 0

    text_test = ("Example: This code creates a window with a Listbox widget "
                 "that displays a list of programming languages. The insert() "
                 "method adds each item to Listbox at specified index and pack() "
                 "displays Listbox in the window. The GUI runs using mainloop().")

    show_text_widget = Text(window, font=("Consolas", 16), wrap="word", width=80, height=10, bg="#2E2E3E", fg="#FFFFFF", bd=0, padx=10, pady=10)
    show_text_widget.place(x=50, y=150)
    show_text_widget.insert("1.0", text_test)
    show_text_widget.config(state="disabled")

    time_left = time_choice.get()
    start_time = time.time()

    timer_label.config(text=str(time_left))
    countdown()
    
    

def key_pressed(event):
    global time_up
    if time_up:
        return
    char_typed = event.char
    idx = current_index[0]
    if not char_typed:
        return
    show_text_widget.config(state="normal")
    if idx < len(text_test) and char_typed == text_test[idx]:
        show_text_widget.tag_add("correct", f"1.{idx}", f"1.{idx+1}")
        show_text_widget.tag_config("correct", foreground="#4EE44E")
        correct_chars[0] += 1
    else:
        show_text_widget.tag_add("wrong", f"1.{idx}", f"1.{idx+1}")
        show_text_widget.tag_config("wrong", foreground="#FF6B6B")
    current_index[0] += 1
    show_text_widget.config(state="disabled")

def countdown():
    global time_left, time_up
    if time_left > 0:
        time_left -= 1
        timer_label.config(text=str(time_left))
        window.after(1000, countdown)
    else:
        timer_label.config(text="Time's up!")
        time_up = True
        end_test()

# Global variables to store results
final_accuracy = 0
final_wpm = 0

def end_test():
    global final_accuracy, final_wpm
    elapsed_time = time_choice.get() - time_left
    total_chars = len(text_test)

    final_accuracy = (correct_chars[0] / total_chars) * 100
    final_wpm = (correct_chars[0] / 5) / (elapsed_time / 60)
    
    result_label.config(text=f"Accuracy: {final_accuracy:.2f}%   WPM: {final_wpm:.2f}")
    
    plt.bar(["Accuracy", "WPM"], [final_accuracy, final_wpm], color=["green","blue"])
    plt.ylim(0, 150)
    plt.show()

header_label = Label(window, text="Typing Speed Tester", font=("Helvetica", 36, "bold"), bg="#1E1E2F", fg="#FFD700")
header_label.pack(pady=10)

chooseTime_label = Label(window, text="Choose Time:", font=("Helvetica",14,"bold"), bg="#1E1E2F", fg="#FFFFFF")
chooseTime_label.place(x=50, y=80)

time_choice = IntVar(value=60)

r1 = Radiobutton(window, text="60s", variable=time_choice, value=60, font=("Helvetica", 12), bg="#1E1E2F", fg="#FFFFFF", selectcolor="#3E3E50", activebackground="#1E1E2F")
r2 = Radiobutton(window, text="180s", variable=time_choice, value=180, font=("Helvetica", 12), bg="#1E1E2F", fg="#FFFFFF", selectcolor="#3E3E50", activebackground="#1E1E2F")
r3 = Radiobutton(window, text="240s", variable=time_choice, value=240, font=("Helvetica", 12), bg="#1E1E2F", fg="#FFFFFF", selectcolor="#3E3E50", activebackground="#1E1E2F")

r1.place(x=170, y=80)
r2.place(x=240, y=80)
r3.place(x=320, y=80)

start_button = Button(window, text="Start Test", font=("Helvetica",18,"bold"), bg="#FFD700", fg="#1E1E2F", width=15, command=show_text, activebackground="#FFB800", bd=0)
start_button.place(x=450, y=70)

timer_label = Label(window, text="0", font=("Helvetica",36,"bold"), bg="#1E1E2F", fg="#00FFFF")
timer_label.place(x=850, y=70)

result_label = Label(window, text="", font=("Helvetica",20,"bold"), bg="#1E1E2F", fg="#00FFFF")
result_label.place(x=200, y=600)

window.bind("<Key>", key_pressed)

window.mainloop()
