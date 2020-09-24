from selenium import webdriver


def _scroll_down_page(driver, speed=8):
    # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    current_scroll_position, new_height = 0, 1
    while current_scroll_position <= new_height:
        current_scroll_position += speed
        driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
        new_height = driver.execute_script("return document.body.scrollHeight")


def get_photos_urls(chromedriver_path: str, url: str) -> list:
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    browser = webdriver.Chrome(chromedriver_path, options=options)
    browser.get(url)
    browser.implicitly_wait(5)
    _scroll_down_page(browser, speed=8)
    browser.find_element_by_id("pushAd_disagree_button").click()
    browser.implicitly_wait(5)
    offers_elements = browser.find_elements_by_class_name("offer_figure")
    photos = [offer.find_element_by_class_name("figure_main-photo").get_attribute("src") for offer in offers_elements]
    print("Found {} photo urls".format(len(photos)))
    browser.close()
    browser.quit()
    return photos


def dupa(chromedriver_path: str, url: str) -> list:
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(chromedriver_path, options=options)
    browser.get(url)
    return browser.page_source
