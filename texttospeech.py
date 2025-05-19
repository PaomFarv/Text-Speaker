import customtkinter as ctk
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

def placeholder_text(event):
    textbox.delete("0.0", "end")

def clear():
    textbox.delete("0.0", "end")
    save_btn.pack_forget()

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
        save_btn.pack(pady=(10, 5))

    elif voice == "Voice 2 (UK)":
        feedback.configure(text="")
        engine.setProperty('voice', voices[1].id)
        engine.say(user_text)
        engine.runAndWait()
        save_btn.pack(pady=(1, 1))

    else:
        feedback.configure(text="You need to select a voice.")
        return

def save_audio():
    user_text = textbox.get("0.0", "end").strip()
    if not user_text:
        feedback.configure(text="No input text found.")
        return
    voice = picked_voice.get()      

    if voice == "Voice 1 (US)":
        engine.setProperty('voice', voices[0].id)
        engine.save_to_file(user_text, 'output1.mp3')
        save_btn.configure(text="Audio Saved!", text_color="green")

    elif voice == "Voice 2 (UK)":
        engine.setProperty('voice', voices[1].id)
        engine.save_to_file(user_text, 'output2.mp3')
        save_btn.configure(text="Audio Saved!", text_color="green")

    else:
        feedback.configure(text="You need to select a voice.")
        return

app = ctk.CTk()
app.title("Text Speaker")
app.geometry("500x620")
app.resizable(False, False)

# Main Frame
main_frame = ctk.CTkFrame(master=app, border_width=2, corner_radius=15)
main_frame.pack(expand=True, fill="both", padx=15, pady=15)

# Header
header = ctk.CTkLabel(
    master=main_frame,
    text="Text Speaker",
    font=("Segoe UI Black", 48),
    text_color="white"
)
header.pack(pady=(20, 10))

# Voice Picker
picked_voice = ctk.StringVar()
voice_menu = ctk.CTkOptionMenu(
    master=main_frame,
    values=["Voice 1 (US)", "Voice 2 (UK)"],
    font=("Segoe UI", 18),
    text_color="black",
    width=400,
    corner_radius=10,
    variable=picked_voice
)
voice_menu.set("Select Voice")
voice_menu.pack(pady=(0, 20))

# Textbox
textbox = ctk.CTkTextbox(
    master=main_frame,
    fg_color="#1E1E1E",
    font=("Consolas", 18),
    text_color="white",
    corner_radius=10,
    wrap="word"
)
textbox.pack(fill="both", expand=True, padx=10, pady=(0, 20))
textbox.insert("0.0", "Insert your text here...")
textbox.bind("<Button-1>", placeholder_text)

# Button Frame (centered)
btn_frame = ctk.CTkFrame(master=main_frame, fg_color="transparent")
btn_frame.pack()

play_btn = ctk.CTkButton(
    master=btn_frame,
    text="▶ Play",
    font=("Segoe UI", 16, "bold"),
    command=text_to_speech,
    corner_radius=12,
    fg_color="#4CAF50",
    hover_color="#388E3C",
    width=150
)
play_btn.grid(row=0, column=0, padx=(0, 10), pady=(0, 10))

clear_btn = ctk.CTkButton(
    master=btn_frame,
    text="🗑️ Clear",
    font=("Segoe UI", 16, "bold"),
    command=clear,
    corner_radius=12,
    fg_color="#F44336",
    hover_color="#C62828",
    width=150
)
clear_btn.grid(row=0, column=1, padx=(10, 0), pady=(0, 10))

# Save Button (Initially Hidden)
save_btn = ctk.CTkButton(
    master=main_frame,
    text="💾 Save Audio",
    font=("Segoe UI", 16, "bold"),
    command=save_audio,
    corner_radius=12,
    fg_color="Black",
    hover_color="#1976D2",
    width=400
)
save_btn.pack_forget()

# Feedback Label (consistent spacing)
feedback = ctk.CTkLabel(
    master=main_frame,
    text="",
    font=("Segoe UI", 18, "bold"),
    text_color="red"
)
feedback.pack(pady=(5, 0))

app.mainloop()
