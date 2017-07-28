# DRIVER
#import
from selenium import webdriver
#make new driver
self.driver = webdriver.xxxx()
#driver types
webdriver.Firefox
webdriver.FirefoxProfile
webdriver.Chrome
webdriver.ChromeOptions
webdriver.Ie
webdriver.Opera
webdriver.PhantomJS
webdriver.Remote
webdriver.DesiredCapabilities
webdriver.ActionChains
webdriver.TouchActions
webdriver.Proxy


# FINDING ELEMENTS
driver.find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector


# WAIT FOR ELEMENTS
#import
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

try:
    element = WebDriverWait(driver, 5).until(
        EC.title_is
        EC.title_contains
        EC.presence_of_element_located
        EC.visibility_of
        EC.presence_of_all_elements_located
        EC.text_to_be_present_in_element
        EC.text_to_be_present_in_element_value
        EC.frame_to_be_available_and_switch_to_it
        EC.invisibility_of_element_located
        EC.element_to_be_clickable
        EC.staleness_of
        EC.element_to_be_selected
        EC.element_located_to_be_selected
        EC.element_selection_state_to_be
        EC.element_located_selection_state_to_be
        EC.alert_is_present
        EC.visibility_of_element_located(
            (By.NAME, 'name')
            (By.ID, 'id')
            (By.LINK_TEXT, 'link text')
            (By.PARTIAL_LINK_TEXT, 'partial link text')
            (By.TAG_NAME, 'tag name')
            (By.CLASS_NAME, 'class name')
            (By.CSS_SELECTOR, 'css selector')
            (By.XPATH, 'xpath')
        )
    )
except ExceptionType:


# EXCEPTION TYPES
#import
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException


# ASSERTIONS
self.assertEqual(a, b)
assertTrue('A'.isupper())
assertFalse('b'.isupper())
assertIn(a, driver.title)
assertEqual(a, b)
assertNotEqual(a, b)
assertTrue(x)
assertFalse(x)
assertIs(a, b)
assertIsNot(a, b)
assertIsNone(x)
assertIsNotNone(x)
assertIn(a, b)
assertNotIn(a, b)
assertIsInstance(a, b)
assertNotIsInstance(a, b)


# EXECUTE JS
driver.execute_script()
# hide element
document.getElementById('id').style.display = 'none';
document.getElementByClassName('class').style.display = 'none';
document.getElementByName('name').style.display = 'none';
document.evaluate ('path', document,null,XPathResult.FIRST_ORDERED_NODE_TYPE,null).singleNodeValue.style.display = 'none';
# remove element
document.getElementById('id').remove();
document.getElementByClassName('class').remove();
document.getElementByName('name').remove();
document.evaluate('path', document, null, XPathResult.FIRSTORDERED_NODE_TYPE,null).singleNodeValue.remove();


# SELECT BOXES
#import
from selenium.webdriver.support.ui import Select

select = Select(driver.find_element_by_xxx())
select.select_by_index(index)
select.select_by_visible_text('TEXT')
select.select_by_value(value)
# deselect all options
select.deselect_all()
# get all opitions
options = select.options


# CLICK ELEMENT
driver.find_element_by_xxx().click()


# FILL TEXT FIELD
driver.find_element_by_xxx().clear()
driver.find_element_by_xxx().send_keys('TEXT')


# CHECK AND UNCHECK CHECK BOXES
# to see if checked or not
driver.find_element_by_xxx().is_selected()
# to check
if driver.find_element_by_xxx().is_selected() is false:
    driver.find_element_by_xxx().click()
# to uncheck
if driver.find_element_by_xxx().is_selected() is true:
    driver.find_element_by_xxx().click()


# FIND IF ELEMENT EXISTS IN DOM
if len(driver.find_elements_by_xxxx()) > 0:
    # element exists

# GET TEXT FROM ELEMENT
driver.find_element_by_xxx().text

# UPLOAD A FILE
driver.find_element_by_xxx().send_keys('PATH TO FILE')

# ALERTS
driver.switch_to.alert.accept()
driver.switch_to.alert.dismiss()


# RANDOM DRIVER ELEMENTS
driver.page_source
driver.title
driver.current_url
driver.manage().delete_all_cookies()
driver.get_window_size()
driver.set_window_size(width, height)
driver.maximize_window()
driver.quit()

