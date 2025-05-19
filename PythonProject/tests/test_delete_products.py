import time
from utils.helpers import login_admin


def test_delete_some_products(browser):
    login_admin(browser, "http://localhost")
    browser.find_element("xpath", "//a[contains(text(), 'Catalog')]").click()
    browser.find_element("xpath", "//a[contains(text(), 'Products')]").click()

    def delete_product(product_name):
        browser.find_element("input[name='filter_name']").clear()
        browser.find_element("input[name='filter_name']").send_keys(product_name)
        browser.find_element("id", "button-filter").click()
        time.sleep(2)
        checkbox = browser.find_element("name", "selected[]")
        checkbox.click()
        browser.find_element("css selector", "button[data-original-title='Delete']").click()
        alert = browser.switch_to.alert
        alert.accept()
        time.sleep(2)

    delete_product("Apple Mouse")
    delete_product("Apple Keyboard")
