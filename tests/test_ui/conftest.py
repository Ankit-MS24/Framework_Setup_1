import pytest
import logging
from selenium import webdriver




@pytest.fixture(scope="session")
def setup_browser():
    driver = webdriver.Chrome()
    driver.get("https://preprod.mobilesentrix.com/")
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield  driver     # Pass driver instance to test
    driver.quit()     # Cleanup after test execution

@pytest.fixture(scope="session")
def setup_logging():
    logging.basicConfig(level=logging.INFO,filename ="test.log", format="%(asctime)s - %(levelname)s - %(message)s")
    return logging.getLogger()

