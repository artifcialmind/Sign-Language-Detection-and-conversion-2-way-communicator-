import tkinter as tk
import tkinter.font
from brightness import start
from speech import get_signs, speech2text
from PIL import ImageTk
root = tk.Tk()
canvas = tk.Canvas(root, width=1000, height=600)
canvas.grid(columnspan=4, rowspan=4)


def real_time():
    corrected_sentence, sentence_taken = start()
    root7 = tk.Toplevel(root)
    root7.geometry("500x500")
    text = tk.Text(root7, height=500, width=500, background="light blue")
    text.place(x=0, y=100)
    text.insert(tk.INSERT, f"Sentence_taken: {sentence_taken}\nCorrect_sentence: {corrected_sentence}")
    root7.mainloop()


def speech_text_to_sign_command():
    root2 = tk.Toplevel(root)
    canvas2 = tk.Canvas(root2, width=800, height=500)
    canvas2.create_image((600, 700), image=img, anchor="center")
    canvas2.grid(columnspan=4, rowspan=4)
    # buttons
    btn3_text = tk.StringVar()
    btn3_text.set("Text to Sign")
    btn3 = tk.Button(root2, textvariable=btn3_text, font=font_1, command=lambda: text_to_sign_command(), width=25
                     , height=3, background="purple",
                     foreground="white")
    btn3.grid(column=1, row=3)
    btn4_text = tk.StringVar()
    btn4_text.set("Speech to Sign")
    btn4 = tk.Button(root2, textvariable=btn4_text,font=font_1, width=25, height=3, background="purple",
                     foreground="white", command=lambda: speech_to_sign_command())
    btn4.grid(column=3, row=3)
    # functions


    def speech_to_sign_command():
        root2.destroy()
        root4 = tk.Toplevel(root)
        root4.geometry("800x500")
        instruction = tk.Label(root4, text="Enter Time duration: ", font="Arabic")
        instruction.place(x=300, y=100)
        text_widget = tk.Text(root4, height=2, width=30)
        text_widget.place(x=400, y=200)
        # buttons
        btn5_text = tk.StringVar()
        btn5 = tk.Button(root4, textvariable=btn5_text, height=2, width=20, background="purple",
                         foreground="white", command=lambda: get_signs(speech2text(int(text_widget.get(1.0, "end-1c")))))
        btn5_text.set("Listen")
        btn5.place(x=400, y=300)
        root4.mainloop()


    def text_to_sign_command():
        root2.destroy()
        root3 = tk.Toplevel(root)
        root3.geometry('800x500')
        instruction = tk.Label(root3, text="Enter Text below: ", font="Arabic")
        instruction.place(x=300, y=100)
        # text widget
        text_widget = tk.Text(root3, height=200, width=300)
        text_widget.place(x=0, y=200)
        # getting signs
        btn5_text = tk.StringVar()
        btn5 = tk.Button(root3, textvariable=btn5_text, command=lambda: get_signs(text_widget.get(1.0, "end-1c")),
                         height=2, width=20, background="purple",
                         foreground="white")
        btn5_text.set("Convert")
        btn5.place(x=300, y=50)
        root3.mainloop()
    root2.mainloop()


# button
img = ImageTk.PhotoImage(file="C:/Users/91797/OneDrive/Desktop/2 way communicator/Images/sign-language-alphabet-hand-drawn-style_23-2147872270.jpg")
canvas.create_image((600, 1000), image=img, anchor="center")
btn1_text = tk.StringVar()
font_1 = tkinter.font.Font(weight="bold")
btn1 = tk.Button(root, textvariable=btn1_text, font=font_1, width=25, height=2, background="red",
                 foreground="white", command=lambda: real_time())
btn1_text.set("Sign language Detection")
btn1.grid(column=0, row=3)
btn2_text = tk.StringVar()
font_2 = tkinter.font.Font(weight="bold")
btn2 = tk.Button(root, textvariable=btn2_text,font=font_2, command=lambda: speech_text_to_sign_command(), width=20, height=2, background="red",
                 foreground="white")
btn2_text.set("Speech/text To Sign")
btn2.grid(column=3, row=3)
root.mainloop()
