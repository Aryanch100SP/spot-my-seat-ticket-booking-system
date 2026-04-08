from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import random

def get_random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        # Add more diverse User-Agents here
    ]
    return random.choice(user_agents)

def scrape_cinema_halls_with_selenium():
    url = "https://in.bookmyshow.com/explore/home/city/delhi-ncr"

    options = Options()
    options.add_argument(f"user-agent={get_random_user_agent()}")
    options.add_argument("--headless") 
    options.add_argument("--no-sandbox") 

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    # Explicitly wait for the page to load (adjust timeout as needed)
    time.sleep(5) 

    # Get the page source and parse it with BeautifulSoup
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")

    # **Crucial: Inspect the BookMyShow website's HTML structure to find the correct elements**
    # This is a more general approach. You might need to adjust based on the actual HTML
    cinema_halls = soup.find_all("a", class_="__venue-name") 

    hall_names = []
    for hall in cinema_halls:
        hall_names.append(hall.text.strip())

    driver.quit()  # Close the browser

    return hall_names

if __name__ == "__main__":
    hall_names = scrape_cinema_halls_with_selenium()
    if hall_names:
        print("List of Cinema Halls:")
        for hall in hall_names:
            print(hall)
