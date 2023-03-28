import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

url = "https://www.zapimoveis.com.br/venda/casas/pe+recife/onde=,Pernambuco,Recife,,,,,,BR%3EPernambuco%3ENULL%3ERecife,&tipos=casa_residencial&transacao=venda"

# Set up the webdriver and navigate to the webpage
driver = webdriver.Chrome()
driver.get(url)

# Find all the card elements and click on each of them
cards = driver.find_elements_by_class_name('card-listing')
for card in cards:    
    try:
        card.click()
        # Wait for the clicked page to load
        driver.implicitly_wait(10)
        
        # Scrape information from the clicked page here
        # ...
        
        # Go back to the original page
        driver.back()
        
    except NoSuchElementException:
        print('Element not found')
        
driver.quit()
