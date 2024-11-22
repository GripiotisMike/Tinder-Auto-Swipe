from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configure Chrome browser options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Launch the browser and navigate to Tinder
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")
time.sleep(2)

# Decline cookies or privacy settings
decline = driver.find_element(By.XPATH, '//*[@id="s-547617529"]/div/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]')
decline.click()
time.sleep(2)

# Click the login button
login = driver.find_element(By.XPATH, '//*[@id="s-547617529"]/div/div[1]/div/main/div[1]/div/div/div/div/'
                                      'header/div/div[2]/div[2]/a/div[2]/div[2]')
login.click()
time.sleep(2)

# Select Facebook login
facebook = driver.find_element(By.XPATH, '//*[@id="s2018968691"]/main/div/div/div[1]/div/div/div[2]'
                                         '/div[2]/span/div[2]/button/div[2]/div[2]/div/div')
facebook.click()
time.sleep(3)

# Switch to the Facebook login popup window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

# Input Facebook credentials
email = driver.find_element(By.XPATH, '//*[@id="email"]')
email.send_keys("YOUR_EMAIL")  # Replace with your email or use environment variables
password = driver.find_element(By.XPATH, '//*[@id="pass"]')
password.send_keys("YOUR_PASSWORD")  # Replace with your password or use environment variables
password.send_keys(Keys.ENTER)
time.sleep(5)

# Switch back to the Tinder main window
driver.switch_to.window(base_window)
time.sleep(3)

# Allow location access
location = driver.find_element(By.XPATH, '//*[@id="s2018968691"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
location.click()
time.sleep(3)

# Decline notifications
not_interested = driver.find_element(By.XPATH, '//*[@id="s2018968691"]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
not_interested.click()
time.sleep(5)

# Locate the "Like" button
like = driver.find_element(By.XPATH, '//*[@id="s-547617529"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/'
                                     'div/div[3]/div/div[4]/button/span/span')

# Automate swiping right (liking profiles) indefinitely
while True:
    like.click()
    time.sleep(2)
