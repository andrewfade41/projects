from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import requests
def telegram_bot(bot_message):
    
    bot_token = ""
    bot_chatID = ''

    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
try:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options = chrome_options)
    # Selenium sürücüsünü başlatın (örneğin, ChromeDriver)
    # driver = webdriver.Chrome("path_to_chromedriver")

    # Web sayfasını yükleyin
    driver.get("https://mobilhastane.omu.edu.tr/MiaMedRandevu/")
    time.sleep(3)
    # Düğmeyi bulmak için XPath kullanın
    button = driver.find_element(By.XPATH, "//*[@id='Btnuyarikapatweb']")

    # Düğmeye tıklayın
    button.click()
    time.sleep(3)
    button = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div/div[2]/div/div/p/button")

    # Düğmeye tıklayın
    button.click()
    time.sleep(3)
    button = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div/div[9]/div/a/img")

    # Düğmeye tıklayın
    button.click()
    time.sleep(3)
    # button = driver.find_element(By.XPATH, "//*[@id='step-1']/div/table/tbody/tr[3]/td[2]/a")
    # //*[@id="step-1"]/div/table/tbody/tr[3]/td[2]/a/text()
    # Düğmeye tıklayın
    button = driver.find_element(By.XPATH,"//a[contains(@onclick, 'Step03Operation(724)')]")

    # print(button)
    
    status = button.text != "DOLU"
    # button.click()
    if status:
        telegram_bot("randevu var")
    time.sleep(3)
    # Tarayıcıyı kapatın
    driver.quit()
except Exception as e:
    telegram_bot(f"randevu hatası {e}")
