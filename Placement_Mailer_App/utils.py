def load_emails(path):
    emails = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            email = line.strip().replace("<","").replace(">","")
            if "@" in email and "." in email:
                emails.append(email)
    return emails

