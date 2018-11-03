from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time
from PIL import Image
from io import BytesIO
from seleniumslicer.pageslicer import save_element


stock = sys.argv[1]
driver = webdriver.Chrome("c:/ChromeDriver/chromedriver.exe")
driver.get("http://www.google.com/search?q="+stock+"+stock")
driver.maximize_window()
yeartab = driver.find_elements_by_class_name('PVZpFf')[5]
driver.execute_script("arguments[0].click()", yeartab);
yeartab.click()
time.sleep(5)
chart = driver.find_elements_by_class_name('knowledge-finance-wholepage-chart__y-tick-label')[0]
save_element(driver, chart, './ChartCapture/'+stock+'.png')
assert "Google Search" in driver.title
driver.close()
