# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # ✅ important
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")  # ✅ required for CI
    chrome_options.add_argument("--disable-dev-shm-usage")  # ✅ prevent memory issues

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    yield driver
    driver.quit()
