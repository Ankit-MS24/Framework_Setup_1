from operator import index
from time import sleep
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from allure import step
import traceback

@pytest.mark.order(1)
@pytest.mark.ui
def test_valid_login(setup_browser):
    """Test valid login with robust click handling"""
    driver = setup_browser

    with step("Click On My Account"):
        account_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//li[@class='ms-account']/a"))
        )
        try:
            account_button.click()
        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].click();", account_button)

    with step("Enter Username and Password"):
        driver.find_element(By.NAME, "useremail").send_keys("admin")
        driver.find_element(By.NAME, "userpassword").send_keys("india123")

        #sleep(10)

    with step("Click Login Button"):
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "performLoginBtn"))
        )
        try:
            login_button.click()
            sleep(10)
        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].click();", login_button)

    with step("Verify Login Success"):
        assert "Cell Phone Repair Parts | iPhone Parts Wholesale | Samsung Parts Supplier - MobileSentrix" in driver.title


    with step("Click On My Account"):
        acc_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//li[@class='ms-account']/a"))
        )

        try:
            acc_button.click()
        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].click();", acc_button)

    with step("Click On My My Dashboard"):
        dash_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='My Dashboard']"))
        )

        try:
            dash_button.click()
        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].click();", dash_button)

    with step("Verify My Dashboard Page"):
        assert "My Account" in driver.title



@pytest.mark.order(2)
@pytest.mark.ui
def test_access_dashboard(setup_browser):
    """Test access to user cart page after login"""
    driver = setup_browser

    with step("Click On Cart"):
        cart_button = WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='cart-button']"))
        )
        try:
            cart_button.click()
        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].click();", cart_button)

    with step("Click On View Cart"):
        view_cart = WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='cartblock']/div/div[1]/a"))
        )
        try:
            view_cart.click()
        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].click();", view_cart)

    with step("Verify View Cart Page is Displayed"):
        assert "Shopping Cart" in driver.title or "Shopping Cart" in driver.current_url


@pytest.mark.order(3)
@pytest.mark.ui
def test_lcd_buyback(setup_browser):
    driver = setup_browser

    with step("Click On My Account"):
        account_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//li[@class='ms-account']/a"))
        )
        try:
            account_button.click()
        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].click();", account_button)

    with step("Enter Username and Password"):
        driver.find_element(By.NAME, "useremail").send_keys("admin")
        driver.find_element(By.NAME, "userpassword").send_keys("india123")

        #sleep(10)

    with step("Click Login Button"):
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "performLoginBtn"))
        )
        try:
            login_button.click()
            sleep(10)
        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].click();", login_button)

    with step("Verify Login Success"):
        assert "Cell Phone Repair Parts | iPhone Parts Wholesale | Samsung Parts Supplier - MobileSentrix" in driver.title


    with step("Click On My Account"):
        acc_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//li[@class='ms-account']/a"))
        )

        try:
            acc_button.click()
        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].click();", acc_button)


    with step("Click On Lcd Buyback"):
        lbb_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//li/a[@title='LCD Buyback']"))
        )
        try:
            lbb_button.click()
        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].click();", lbb_button)

    with step("Than Click On Start New Buyback Request"):
        bbr_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='BsOrder_newRequest']"))
        )
        try:
            bbr_button.click()
        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].click();", bbr_button)

    with step("Enter The Product Quantity"):
        try:
            # **Wait for order form to load**
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "order-form-li")))

            # **Find all input fields dynamically**
            all_input_fields = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//*[@id='order-form-li']//input[@type='text']"))
            )

            total_fields = len(all_input_fields)
            print(f"Total input fields found: {total_fields}")

            if total_fields == 0:
                print("No input fields found.")
            else:
                # **Loop through each input field and enter values**
                for index, input_field in enumerate(all_input_fields):
                    try:
                        driver.execute_script("arguments[0].scrollIntoView();", input_field)  # Ensure visibility

                        # **Ensure Input is Editable**
                        #driver.execute_script("arguments[0].removeAttribute('readonly');", input_field)
                        #driver.execute_script("arguments[0].removeAttribute('disabled');", input_field)

                        input_field.clear()
                        input_field.send_keys(str((index + 1) * 10))  # Example: 10, 20, 30, ...
                        sleep(2)  # Short delay for stability

                    except Exception as e:
                        print(f"Error interacting with field {index}: {e}")
                        traceback.print_exc()

        except Exception as e:
            print(f"Error encountered: {e}")
            traceback.print_exc()

        sleep(5)  # Observe changes before closing
        driver.quit()









