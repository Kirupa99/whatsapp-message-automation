import csv
import os
import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Message

video_path = os.path.abspath("Kirupa_Raghav_einvite.mp4")
contacts = []

# Read contacts from CSV
with open("myContacts.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        contacts.append(row)

for contact in contacts:
    print(contact)

# Launch WhatsApp Web
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
print("Please scan the QR code in WhatsApp Web...")
time.sleep(60)  # wait for login

for contact in contacts:
    nickname = contact['Nickname']
    phone = contact['Phone'].replace("+", "")
    message = Message.message_template.format(nickname=nickname)

    # Open chat by phone number
    url = f"https://web.whatsapp.com/send?phone={phone}"
    driver.get(url)

    try:
        # Wait for the input box to load
        input_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
        )
    except:
        print(f"Chat failed to load for {nickname}")
        continue

    # Copy message to clipboard
    pyperclip.copy(message)
    input_box.click()  # focus input
    input_box.send_keys(Keys.COMMAND, 'v')  # CMD+V to paste on Mac
    input_box.send_keys(Keys.ENTER)  # send message
    print(f"✅ Sent message to {nickname}")

    # Send video attachment
    try:
        attach_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//span[@data-icon="clip"]'))
        )
        attach_button.click()

        file_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="file"]'))
        )
        file_input.send_keys(video_path)

        send_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send"]'))
        )
        send_button.click()
        print(f"✅ Sent video to {nickname}")
    except Exception as e:
        print(f"Could not send video to {nickname}: {e}")

    time.sleep(5)

driver.quit()
