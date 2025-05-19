import time

def login_admin(driver, url, username="admin", password="admin"):
    driver.get(f"{url}/admin/")
    driver.find_element("id", "input-username").send_keys(username)
    driver.find_element("id", "input-password").send_keys(password)
    driver.find_element("css selector", "button[type='submit']").click()
    time.sleep(2)
