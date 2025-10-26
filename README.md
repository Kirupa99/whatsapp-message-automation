# 💬 Personalized WhatsApp Messenger  
*Because nobody likes generic “Forwarded” texts 😅*

---

## 🧠 About the Project  
This project started as a personal experiment — I wanted to send out e-invites to my friends via WhatsApp.  
But forwarding the same message to everyone felt too impersonal, and typing each person’s name manually wasn’t practical.  

So I built a small **Python automation script** that reads contact names from a CSV file, personalizes each message (e.g., “Hi John, how are you doing?”), and sends it automatically via **WhatsApp Web** using Selenium.  

Now, every message feels handcrafted — even though I didn’t type it 50 times 😉  

---

## ⚙️ Features  
✅ Reads contacts and nicknames from a CSV file  
✅ Automatically generates personalized messages  
✅ Sends messages safely through WhatsApp Web  
✅ Reuses Chrome session (no repeated QR scans)  
✅ Simple, lightweight, and easy to customize  

---

## 🧩 Tech Stack  
- **Python 3.9+**  
- **Selenium WebDriver**  
- **CSV File Handling**  
- (Optional) **vobject** for `.vcf` to `.csv` contact conversion  

---

## 🚀 Setup & Usage  

1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/whatsapp-message-automation.git
cd whatsapp-message-automation

2️⃣ Create a Virtual Environment
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install selenium vobject

4️⃣ Export Contacts to CSV
If you have contacts in .vcf format, use vobject to convert them to CSV.
Make sure your CSV looks like this:
Full_name,Nickname,Phone
John Doe,John,+44123456789
Nivi Manoj,Nivi,+44798765432

5️⃣ Run the Script
python send_whatsapp_messages.py
The script opens WhatsApp Web in Chrome.
Scan the QR code once (first time only).
Messages will be sent automatically, personalized for each contact.

💡 Example Message
Hi Nivi, how are you doing?

Looks natural and friendly — not like a mass forward 🙌
