# menu.py

def search_google():
    from googlesearch import search
    query = input("Enter your search query: ")
    print("Top 5 results:")
    for url in search(query, num_results=5):
        print(url)

def send_email():
    import smtplib
    from email.mime.text import MIMEText

    sender = input("Your Gmail address: ")
    app_password = input("App password (not your regular password): ")
    receiver = input("Receiver's email: ")
    subject = input("Email Subject: ")
    body = input("Email Body: ")

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, app_password)
            server.send_message(msg)
            print("✅ Email sent!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

def download_website():
    import requests
    from bs4 import BeautifulSoup

    url = input("Enter website URL: ")
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        with open("site.html", "w", encoding="utf-8") as f:
            f.write(soup.prettify())
        print("✅ Website saved as site.html")
    except Exception as e:
        print(f"❌ Failed: {e}")

def menu():
    while True:
        print("\n===== PYTHON CLI MENU =====")
        print("1. Search Google")
        print("2. Send Email")
        print("3. Download Website")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            search_google()
        elif choice == "2":
            send_email()
        elif choice == "3":
            download_website()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid option")

if __name__ == "__main__":
    menu()

