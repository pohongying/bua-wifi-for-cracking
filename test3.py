# import requests
# from bs4 import BeautifulSoup
#
# url = "http://10.0.0.38/a70.htm"
# head = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
# }
#
# r = requests.get(url, headers=head)
#
# print(r.status_code)

# import pyautogui as gui
#
# print("获取当前鼠标的位置：", end="")
# print(gui.position())  # Point(x=1964, y=1338)
# print("获取当前屏幕的大小：", end="")
# print(gui.size())
#
# gui.moveTo(100, 300, duration=1)
#
# gui.click(100, 100, button="left", duration=1)
# gui.click(100, 400, button="right", duration=1)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# 创建 Chrome WebDriver
driver = webdriver.Chrome()

try:
    driver.get("http://10.98.48.6")

    # 使用XPath定位并等待按钮可点击后点击
    button_xpath = '//*[@id="tbody"]/tr/td[6]/button'
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))

    # 获取按钮元素
    button = driver.find_element(By.XPATH, button_xpath)

    # 使用 JavaScript 点击按钮
    driver.execute_script("arguments[0].click();", button)

    # 在这里可以添加其他操作，如等待、获取数据等

except TimeoutException:
    print("等待超时，无法找到可点击的按钮")

finally:
    # 关闭浏览器窗口
    driver.quit()




