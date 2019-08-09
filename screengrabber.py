from selenium import webdriver
DRIVER = 'chromedriver'
driver = webdriver.Chrome(DRIVER)
import pandas as pd
df = pd.read_csv('all_data.csv')
links= list(df['link'])
for i in links:
    driver.get(i)
    screenshot = driver.save_screenshot(r'folder\\'+str(i)+'.png')
    driver.quit()
