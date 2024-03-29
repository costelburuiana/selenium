from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions


class TestWebtable():
  def setup_method(self, method):
    # Headless Chrome
    options = ChromeOptions()
    options.add_argument("--headless=new")
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
  
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_webtable(self):
    self.driver.get("https://demoqa.com/webtables")
    self.driver.set_window_size(1294, 1392)
    self.driver.find_element(By.ID, "addNewRecordButton").click()
    self.driver.find_element(By.ID, "firstName").click()
    self.driver.find_element(By.ID, "firstName").send_keys("FirstName")
    self.driver.find_element(By.ID, "lastName").click()
    self.driver.find_element(By.ID, "lastName").send_keys("Lastname")
    self.driver.find_element(By.ID, "userEmail").click()
    self.driver.find_element(By.ID, "userEmail").send_keys("name@domain.com")
    self.driver.find_element(By.ID, "age").click()
    self.driver.find_element(By.ID, "age").send_keys("35")
    self.driver.find_element(By.ID, "salary").click()
    self.driver.find_element(By.ID, "salary").send_keys("15000")
    self.driver.find_element(By.ID, "department").click()
    self.driver.find_element(By.ID, "department").send_keys("IT")
    self.driver.find_element(By.ID, "submit").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".rt-tr-group:nth-child(4) .rt-td:nth-child(1)").text == "FirstName"
    assert self.driver.find_element(By.CSS_SELECTOR, ".rt-tr-group:nth-child(4) .rt-td:nth-child(2)").text == "Lastname"
    assert self.driver.find_element(By.CSS_SELECTOR, ".rt-tr-group:nth-child(4) .rt-td:nth-child(4)").text == "name@domain.com"
    assert self.driver.find_element(By.CSS_SELECTOR, ".rt-tr-group:nth-child(4) .rt-td:nth-child(5)").text == "15000"
  
