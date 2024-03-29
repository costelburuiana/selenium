from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions

class TestRadiobuttons():
  def setup_method(self, method):
    # Headless Chrome
    options = ChromeOptions()
    options.add_argument("--headless=new")
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
  
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_radiobuttons(self):
    self.driver.get("https://demoqa.com/radio-button")
    self.driver.set_window_size(1278, 1391)
    self.driver.find_element(By.CSS_SELECTOR, ".custom-control:nth-child(2) > .custom-control-label").click()
    self.driver.find_element(By.CSS_SELECTOR, ".col-md-6").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".mt-3").text == "You have selected Yes"
    self.driver.close()
  
