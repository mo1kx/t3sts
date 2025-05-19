import time


def test_search_products(browser):
    browser.get("http://localhost/")
    search_box = browser.find_element("name", "search")

    for keyword in ["Logitech", "Apple"]:
        search_box.clear()
        search_box.send_keys(keyword)
        browser.find_element("css selector", "button.btn-default").click()
        time.sleep(2)
        products = browser.find_elements("css selector", ".product-thumb")
        assert len(products) > 0, f"No products found for keyword '{keyword}'"
