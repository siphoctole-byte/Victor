import customtkinter as ctk

# -----------------------------
# Appearance
# -----------------------------
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# -----------------------------
# Window
# -----------------------------
app = ctk.CTk()

app.title("Victor AI Assistant")
app.geometry("1000x700")

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
# Message Entry
# -----------------------------
message_entry = ctk.CTkEntry(
    app,
    width=700,
    placeholder_text="Type your message..."
)

message_entry.pack(side="left", padx=20, pady=20)

# -----------------------------
# Send Button
# -----------------------------
send_button = ctk.CTkButton(
    app,
    text="Send"
)

send_button.pack(side="left", padx=10)

# -----------------------------
# Clear Button
# -----------------------------
clear_button = ctk.CTkButton(
    app,
    text="Clear"
)

clear_button.pack(side="left", padx=10)

# -----------------------------
# Status
# -----------------------------
status = ctk.CTkLabel(
    app,
    text="Status: Online",
    font=("Segoe UI", 12)
)

status.pack(side="bottom", pady=10)

app.mainloop()