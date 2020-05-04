from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com/')
elem = browser.find_element_by_css_selector('.main > div:nth-child(1) > ul:nth-child(20) > li:nth-child(1) > a:nth-child(1)')
elem
elem.click()
searchElem=browser.find_element_by_css_selector('.search-field')
searchElem.send_keys('zophie')
searchElem.submit()
browser.back()
browser.forward()
browser.refresh()
browser.quit()
