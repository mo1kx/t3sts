import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os


@pytest.fixture(scope="session")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service(
        executable_path="/opt/homebrew/bin/chromedriver")  # или тот путь, который покажет `which chromedriver`
    # Обнови путь при необходимости

    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()
