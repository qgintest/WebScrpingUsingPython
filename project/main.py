import requests
import selectorlib
import time
import sqlite3

# Establish connection
connection = sqlite3.connect("temperature.db")
cursor = connection.cursor()


URL = "https://programmer100.pythonanywhere.com/"

def scrape(url):
    """Scraping page source"""
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tempLabel"]
    return value


def store(extracted):
    formatted_time = time.strftime("%y-%m-%d-%H-%M-%S")

    new_rows = [(formatted_time, extracted)]

    cursor.executemany("INSERT INTO temperature VALUES(?, ?)", new_rows)

    connection.commit()

    # with open("data.txt", 'a') as file:
    #     formatted_time = time.strftime("%y-%m-%d-%H-%M-%S")
    #     file.write(f"{formatted_time},{extracted}\n")

def get_all_rows():
    # Query data
    cursor.execute("SELECT * FROM temperature")
    rows = cursor.fetchall()
    print(rows)

if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)
    store(extracted)
    get_all_rows()