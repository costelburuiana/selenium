from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions

class TestTextbox():
  def setup_method(self, method):
    # Headless Chrome
    options = ChromeOptions()
    options.add_argument("--headless=new")
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
  
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_textbox(self):
    self.driver.get("https://demoqa.com/text-box")
    self.driver.set_window_size(1294, 1392)
    self.driver.find_element(By.ID, "userName").click()
    self.driver.find_element(By.ID, "userName").send_keys("Full Name")
    self.driver.find_element(By.ID, "userEmail").send_keys("name@domain.com")
    self.driver.find_element(By.ID, "currentAddress").send_keys("35 London Rd, Dartford, SE2 XXX")
    self.driver.find_element(By.ID, "permanentAddress").click()
    self.driver.find_element(By.ID, "permanentAddress").click()
    self.driver.find_element(By.ID, "permanentAddress-wrapper").click()
    self.driver.find_element(By.ID, "permanentAddress").send_keys("London, SW")
    self.driver.find_element(By.ID, "permanentAddress").click()
    self.driver.find_element(By.ID, "permanentAddress").click()
    self.driver.find_element(By.ID, "permanentAddress").send_keys("London, SW1A 1AA, UK")
    self.driver.find_element(By.ID, "submit").click()
    self.driver.find_element(By.CSS_SELECTOR, ".border").click()
    assert self.driver.find_element(By.ID, "name").text == "Name:Full Name"
    
  
