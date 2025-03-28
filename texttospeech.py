import customtkinter as ctk
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

def placeholder_text(event):
    textbox.delete("0.0", "end")

def clear():
    textbox.delete("0.0", "end")

def text_to_speech():
    user_text = textbox.get("0.0", "end").strip()
    if not user_text:
        feedback.configure(text="No input text found.")
        return
    
    voice = picked_voice.get()      

    if voice == "Voice 1 (US)":
        feedback.configure(text="")
        engine.setProperty('voice', voices[0].id)
        engine.say(user_text)
        engine.runAndWait()

    elif voice == "Voice 2 (UK)":
        feedback.configure(text="")
        engine.setProperty('voice', voices[1].id)
        engine.say(user_text)
        engine.runAndWait()

    else:
        feedback.configure(text="You need to select a voice.")
        return

app = ctk.CTk()
app.title("Text Speaker")
app.geometry("500x620")

main_frame = ctk.CTkFrame(master=app,border_width=1)
main_frame.pack(expand=True, fill="both", padx=10, pady=10)

header = ctk.CTkLabel(master=main_frame, text="Text Speaker", font=("Segoe UI Black", 65),text_color="white")
header.pack(pady=10)

picked_voice = ctk.StringVar()
voice_menu = ctk.CTkOptionMenu(master=main_frame,values=["Voice 1 (US)","Voice 2 (UK)"],font=("Arial",20,"bold"),text_color="black",width=370,variable=picked_voice)
voice_menu.pack(pady=10)
voice_menu.set("Select Voice")

btn_frame = ctk.CTkFrame(master=main_frame,fg_color="transparent")
btn_frame.pack()

play_btn = ctk.CTkButton(master=btn_frame,text="Play Speech",font=("Arial",15,"bold"),command=text_to_speech, corner_radius=15, fg_color="green", hover_color="darkgreen")
play_btn.pack(side="left",padx=5)

clear_btn = ctk.CTkButton(master=btn_frame,text="Clear",font=("Arial",15,"bold"),command=clear, corner_radius=15, fg_color="red", hover_color="darkred")
clear_btn.pack(side="right",padx=5)

textbox = ctk.CTkTextbox(master=main_frame,fg_color="black",font=("Bahnschrift SemiBold",20))
textbox.pack(fill="both",pady=20,padx=10,expand=True)

textbox.insert("0.0", "Insert your text here...")
textbox.bind("<Button-1>",placeholder_text)

feedback = ctk.CTkLabel(master=main_frame,text="",font=("Arial",20,"bold"),text_color="Red")
feedback.pack()

app.mainloop()
