from selenium import webdriver
from selenium.webdriver.common.by import By





product={}

def getData():
    PATH = "C:\chromedriver\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.amazon.co.jp/s?i=computers&bbn=2151901051&rh=n%3A2127209051%2Cn%3A2151901051%2Cn%3A2151911051%2Cp_n_price_fma%3A2150394051%7C2150395051%2Cp_6%3AAN1VRQENFRJN5%2Cp_n_shipping_option-bin%3A2493950051&dc&language=en&qid=1623672594&rnid=2151901051&ref=sr_pg_1")
    links = driver.find_elements_by_xpath("//a[@class='a-link-normal a-text-normal']")
    gpuNames =  driver.find_elements(By.XPATH,"//span[contains(@class,'a-size-base-plus a-color-base a-text-normal')]")
    prices =  driver.find_elements(By.XPATH,"//span[contains(@class,'a-price-whole')]")
    x,y,z = 1,1,1
    for gpuName in gpuNames:
        gpuName = gpuName.text.split("/")
        gpuName = gpuName[0]
        product[x] = {'title':gpuName}
        x +=1
    for price in prices:
        price = price.text
        price = price.split("¥")
        price = price[1]
        product[y]['price'] = price
        y +=1
    for linkk in links:
        s = linkk.get_attribute("href").split("dp/")
        s = s[1].split("/ref")
        product[z]['ASIN'] = s[0]
        z +=1
    print(product)

