from selenium import webdriver
from time import sleep
my_driver = webdriver.Chrome()
my_driver.get("https://github.com/vinta/awesome-python")
#info = my_driver.find_element_by_xpath('/html/body/div')
print(my_driver.page_source.count('<a'))


