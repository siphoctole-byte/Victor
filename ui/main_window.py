import customtkinter as ctk
from core.assistant import Assistant

# -----------------------------
# Victor AI
# -----------------------------
victor = Assistant()

# -----------------------------
# Appearance
# -----------------------------
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# -----------------------------
# Main Window
# -----------------------------
app = ctk.CTk()
app.title("Victor AI Assistant")
app.geometry("1000x700")

# -----------------------------
# Send Message Function
# -----------------------------
def send_message(event=None):
    message = message_entry.get().strip()

    if not message:
        return

    chat_box.insert("end", f"You: {message}\n")

    reply = victor.reply(message)

    chat_box.insert("end", f"Victor: {reply}\n\n")

    message_entry.delete(0, "end")

    chat_box.see("end")


# -----------------------------
# Clear Chat Function
# -----------------------------
def clear_chat():
    chat_box.delete("1.0", "end")
    chat_box.insert("end", "Victor: Chat cleared.\n\n")


# -----------------------------
# Title
# -----------------------------
title = ctk.CTkLabel(
    app,
    text="VICTOR AI ASSISTANT",
    font=("Segoe UI", 30, "bold")
)

title.pack(pady=15)

# -----------------------------
# Chat Box
# -----------------------------
chat_box = ctk.CTkTextbox(
    app,
    width=900,
    height=450,
    font=("Consolas", 14)
)

chat_box.pack(pady=10)

chat_box.insert("end", "Victor: Welcome! I'm ready to help you.\n\n")

# -----------------------------
# Bottom Frame
# -----------------------------
bottom_frame = ctk.CTkFrame(app)
bottom_frame.pack(fill="x", padx=20, pady=20)

# -----------------------------
# Message Entry
# -----------------------------
message_entry = ctk.CTkEntry(
    bottom_frame,
    placeholder_text="Type your message...",
    width=650
)

message_entry.pack(side="left", padx=10)

# -----------------------------
# Send Button
# -----------------------------
send_button = ctk.CTkButton(
    bottom_frame,
    text="Send",
    command=send_message
)

send_button.pack(side="left", padx=10)

# -----------------------------
# Clear Button
# -----------------------------
clear_button = ctk.CTkButton(
    bottom_frame,
    text="Clear",
    command=clear_chat
)

clear_button.pack(side="left", padx=10)

# -----------------------------
# Status Bar
# -----------------------------
status = ctk.CTkLabel(
    app,
    text="Status: Online",
    font=("Segoe UI", 12)
)

status.pack(side="bottom", pady=10)

# -----------------------------
# ENTER Key
# -----------------------------
message_entry.bind("<Return>", send_message)

# -----------------------------
# Run Victor
# -----------------------------
app.mainloop()