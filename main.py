import sqlite3

import requests
import selectorlib
import smtplib, ssl
import os
import time

from pyexpat.errors import messages

URL = "https://programmer100.pythonanywhere.com/tours/"


class Event:
    def scrape(self, url):
        """Scraping page source"""
        response = requests.get(url)
        source = response.text
        return source

    def extract(self, source):
        extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
        value = extractor.extract(source)["tours"]
        return value


class Email:
    def email(self, message):
        host = "smtp.gmail.com"
        port = 465

        username = "aeendale@gmail.com"
        password = os.getenv("PASSWORD")

        receiver = "aeendale@gmail.com"
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message.encode('utf-8'))

        print("Email Sent")


class Storage:

    def __init__(self, argument):
        self.connection = sqlite3.connect("data.db")
        print("Storage Class: " + argument)

    def store(self, extracted):
        with open("data.txt", 'a') as file:
            file.write(extracted + "\n")

    def read(self, extracted):
        with open('data.txt', 'r') as file:
            return file.read()


if __name__ == "__main__":
    while True:
        event = Event()
        send = Email()
        storage = Storage(argument="argument")
        scraped = event.scrape(URL)
        extracted = event.extract(scraped)
        print(extracted)
        content = storage.read(extracted)
        if extracted != "No upcoming tours":
            if extracted not in content:
                storage.store(extracted)
                send.email(message="New Event Detected!")
        time.sleep(2)