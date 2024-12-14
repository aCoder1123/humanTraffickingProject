from selenium import webdriver
from selenium.webdriver.common.by import By
element_list = []
urls = [f"https://www.aa.com/en-us/sitemap/city-to-city-flights/page-{i}" for i in range(1, 29)]
outputFile = open("aaOutput.tsv", 'w')

outputFile.write("Origin\tDestination\t")

driver = webdriver.Firefox()
for url in urls:
    driver.get(url)
    title = driver.find_elements(By.TAG_NAME, "ul")
    data = title[2].text
    dataList = data.split("\n")
    for flight in dataList:
        flightData = flight.replace(' to ', '\t')
        outputFile.write(f"\n{flightData}\t")

driver.close()