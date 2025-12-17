import tkinter as tk
from tkinter import filedialog, messagebox
from mailer import send_bulk_mail

email_file = ""
attachment_file = ""

def choose_email_file():
    global email_file
    email_file = filedialog.askopenfilename(
        title="Select Email List",
        filetypes=[("Text files", "*.txt"), ("CSV files", "*.csv")]
    )

def choose_attachment():
    global attachment_file
    attachment_file = filedialog.askopenfilename(
        title="Select Resume (PDF)",
        filetypes=[("PDF files", "*.pdf")]
    )

def send_mail_action():
    subject = subject_entry.get().strip()
    body = body_text.get("1.0", tk.END).strip()

    if not email_file or not subject or not body:
        messagebox.showerror("Error", "Please fill all required fields")
        return

    try:
        count = send_bulk_mail(email_file, subject, body, attachment_file)
        messagebox.showinfo("Success", f"Mail sent successfully to {count} emails")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def start_gui():
    root = tk.Tk()
    root.title("Placement Mailer Application")
    root.geometry("520x520")

    tk.Button(root, text="Upload Email List (TXT/CSV)", command=choose_email_file).pack(pady=8)
    tk.Button(root, text="Upload Resume (PDF)", command=choose_attachment).pack(pady=8)

    tk.Label(root, text="Email Subject").pack()
    global subject_entry
    subject_entry = tk.Entry(root, width=60)
    subject_entry.pack(pady=5)

    tk.Label(root, text="Email Body").pack()
    global body_text
    body_text = tk.Text(root, width=60, height=12)
    body_text.pack(pady=5)

    tk.Button(root, text="Send Emails", bg="green", fg="white",
              font=("Arial", 11, "bold"), command=send_mail_action).pack(pady=15)

    root.mainloop()
