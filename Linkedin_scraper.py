from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# Start a Selenium webdriver session
driver = webdriver.Chrome()  # or webdriver.Firefox(), etc.
driver.maximize_window()
# Navigate to LinkedIn and login manually
driver.get("https://linkedin.com/uas/login")
# entering username
username = driver.find_element(By.ID, "username")

# In case of an error, try changing the element
# tag used here.

# Enter Your Email Address
username.send_keys("your_mail") 

# entering password
pword = driver.find_element(By.ID, "password")
# In case of an error, try changing the element 
# tag used here.

# Enter Your Password
pword.send_keys("your_password")	 

# Clicking on the log in button
# Format (syntax) of writing XPath --> 
# //tagname[@attribute='value']
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Assuming you've logged in manually
# Navigate to the LinkedIn page you want to scrape
# Navigate to the LinkedIn page you want to scrape
# driver.get("https://www.linkedin.com/company/jpmorganchase/posts/")
driver.get("https://www.linkedin.com/company/blackstonegroup/posts/")


time.sleep(5)

# Scroll to load more posts
SCROLL_PAUSE_TIME = 3

last_height = driver.execute_script("return document.body.scrollHeight")

start_time = time.time()
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

    # Check if 10 seconds have elapsed
    if time.time() - start_time > 10:
        break

# Wait for the page to load completely
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "scaffold-finite-scroll__content")))

# Get the page source and parse it with BeautifulSoup
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# Find the top ten posts
top_posts = soup.find_all("div", class_="feed-shared-update-v2__description-wrapper")
print(len(top_posts))

# update-components-actor display-flex

# Extract information from the top ten posts
for i, post in enumerate(top_posts[:10]):
    # print(post)
    print(f"Post {i+1}:")
    # post_text = post.find("span", class_="break-words").text.strip()
    # print("Post Text:", post_text)
    # Extract post text
    post_text = post.find("span", class_="break-words").text.strip()
    print("Post Text:", post_text)
    
    # Extract post date and time
    # post_date_time = post.find("span", class_="visually-hidden").text.strip()
    # print("Post Date and Time:", post_date_time)
    print()
    # break

# Close the webdriver session
driver.quit()