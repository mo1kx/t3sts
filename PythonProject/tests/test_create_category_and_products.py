from utils.helpers import login_admin
import time


def test_create_category_and_products(browser):
    url = "http://localhost"  # замените на ваш адрес OpenCart
    login_admin(browser, url)

    # Создание категории Devices
    browser.find_element("xpath", "//a[contains(text(), 'Catalog')]").click()
    browser.find_element("xpath", "//a[contains(text(), 'Categories')]").click()
    browser.find_element("css selector", "a[data-original-title='Add New']").click()
    browser.find_element("id", "input-name1").send_keys("Devices")
    browser.find_element("id", "input-meta-title1").send_keys("Devices Meta")
    browser.find_element("css selector", "button[data-original-title='Save']").click()
    time.sleep(2)

    # Добавление товаров
    browser.find_element("xpath", "//a[contains(text(), 'Products')]").click()

    def add_product(name, description):
        browser.find_element("css selector", "a[data-original-title='Add New']").click()
        browser.find_element("id", "input-name1").send_keys(name)
        browser.find_element("css selector", "div.note-editable").send_keys(description)
        browser.find_element("id", "input-meta-title1").send_keys(f"{name} Meta")
        browser.find_element("xpath", "//a[text()='Data']").click()
        browser.find_element("id", "input-model").send_keys(name.lower().replace(" ", "_"))
        browser.find_element("xpath", "//a[text()='Links']").click()
        browser.find_element("input[name='category']").send_keys("Devices")
        time.sleep(1)
        browser.find_element("css selector", ".dropdown-menu li a").click()
        browser.find_element("css selector", "button[data-original-title='Save']").click()
        time.sleep(2)

    add_product("Logitech Mouse", "Wireless mouse")
    add_product("Apple Mouse", "Magic mouse")
    add_product("Logitech Keyboard", "Wireless keyboard")
    add_product("Apple Keyboard", "Magic keyboard")
