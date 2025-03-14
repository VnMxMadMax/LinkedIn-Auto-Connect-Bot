from selenium import webdriver  # Web automation framework
from selenium.webdriver.common.by import By  # Helps locate elements on a webpage
from selenium.webdriver.common.keys import Keys  # Simulates keyboard inputs
from selenium.webdriver.chrome.service import Service  # Manages ChromeDriver service
from selenium.webdriver.chrome.options import Options  # Allows configuring Chrome options
from selenium.webdriver.support.ui import WebDriverWait  # Enables explicit waits
from selenium.webdriver.support import expected_conditions as EC  # Waits for specific conditions
from selenium.common.exceptions import NoSuchElementException, TimeoutException  # Handles exceptions
from selenium.webdriver.common.action_chains import ActionChains  # Simulates user interactions
from webdriver_manager.chrome import ChromeDriverManager  # Manages ChromeDriver installation
import time  # Introduces delays to mimic human behavior
import random  # Generates random delays to avoid detection

# Configure Chrome options to avoid bot detection
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # Prevents LinkedIn from detecting automation
options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Disables automation flag in Chrome
options.add_experimental_option("useAutomationExtension", False)  # Ensures no automation extensions are used

# Initialize WebDriver with ChromeDriver
# Automatically downloads and manages the ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open LinkedIn login page
driver.get("https://www.linkedin.com/login")

# Wait until the login page loads and locate username/password fields
wait = WebDriverWait(driver, 10)
username = wait.until(EC.presence_of_element_located((By.ID, "username")))
password = driver.find_element(By.ID, "password")

# Enter login credentials
username.send_keys("your_email@example.com")  # Replace with your email
password.send_keys("your_password")  # Replace with your password

# Click the login button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Wait until the LinkedIn homepage loads
wait.until(EC.presence_of_element_located((By.ID, "global-nav")))

# Define job role for search
role = "data scientist"  #Change job role

# Iterate through the first 5 pages of search results
for page in range(1, 6):
    print(f"\n🔍 Searching Page {page}...\n")
    
    # Construct the LinkedIn search URL with the specified role and page number
    search_url = f"https://www.linkedin.com/search/results/people/?keywords={role}&page={page}"
    driver.get(search_url)

    # Wait for page to load with a random delay to avoid detection
    time.sleep(random.uniform(4, 6))

    try:
        while True:  # Loop to process all profiles on the current page
            # Scroll multiple times to load dynamic profiles
            for _ in range(5):  # Scrolls down 5 times, 400 pixels per step
                driver.execute_script("window.scrollBy(0, 400);")  # Scroll down
                time.sleep(random.uniform(2, 4))  # Add human-like delay

            # Find all "Connect" buttons on the page
            connect_buttons = driver.find_elements(By.XPATH, "//button[.//span[text()='Connect']]")

            if not connect_buttons:  # If no connect buttons are found, exit the loop
                print("No 'Connect' buttons found on this page.")
                break  # Exit the loop if no more buttons are available

            # Iterate through each "Connect" button and send requests
            for button in connect_buttons:
                try:
                    # Scroll the button into view to make it visible
                    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", button)
                    time.sleep(random.uniform(1, 3))

                    # Move cursor to the button (human-like behavior)
                    actions = ActionChains(driver)
                    actions.move_to_element(button).perform()

                    # Try clicking the button
                    try:
                        button.click()  # Normal click attempt
                    except:
                        driver.execute_script("arguments[0].click();", button)  # JavaScript click fallback

                    time.sleep(random.uniform(2, 5))  # Wait for the pop-up

                    # Click the "Send without a note" button to send the request
                    try:
                        send_without_note_button = WebDriverWait(driver, 5).until(
                            EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Send without a note']]"))
                        )
                        send_without_note_button.click()
                        print("✅ Connection request sent successfully.")
                        time.sleep(random.uniform(2, 4))
                    except TimeoutException:
                        print("⚠️ Skipping profile - 'Send without a note' button not found.")

                except Exception as e:
                    print(f"⚠️ Error clicking 'Connect' button: {e}")

    except KeyboardInterrupt:
        print("Script stopped by user.")
        break  # Allow user to stop the script manually

# Close the browser session
driver.quit()