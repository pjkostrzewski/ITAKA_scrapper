from selenium import webdriver

# WORK IN PROGRESS

chromedriver_path = "/Users/patrykkostrzewski/Downloads/chromedriver"


def __scroll_down_page(driver, speed=8):
    current_scroll_position, new_height= 0, 1
    while current_scroll_position <= new_height:
        current_scroll_position += speed
        driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
        new_height = driver.execute_script("return document.body.scrollHeight")


_url = "https://www.itaka.pl/last-minute/?departureDate=2020-09-23&view=offerList&package-type=wczasy&adults=2&date-from=2020-09-22&promo=lastMinute&order=dateFromAsc&total-price=0&page=1&transport=bus%2Cflight&currency=PLN"
browser = webdriver.Chrome(chromedriver_path)
browser.get(_url)
browser.implicitly_wait(2)

__scroll_down_page(browser, speed=5)
browser.find_element_by_id("pushAd_disagree_button").click()
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
browser.implicitly_wait(15)
photos = browser.find_elements_by_class_name("item_photo")
print(len(photos))
# for photo in photos:
#     print(photo.get_attribute("src"))
# browser.close()
# browser.quit()
# print(browser.find_elements_by_class_name("offer clearfix"))
