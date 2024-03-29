
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options as ChromeOptions

class TestButtons():
  def setup_method(self, method):
    # Headless Chrome
    options = ChromeOptions()
    options.add_argument("--headless=new")
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
 
  
  def test_doubleclick(self):
    self.driver.get("https://demoqa.com/buttons")
    self.driver.set_window_size(1294, 1392)
    self.driver.find_element(By.ID, "doubleClickBtn").click()
    self.driver.find_element(By.ID, "doubleClickBtn").click()
    element = self.driver.find_element(By.ID, "doubleClickBtn")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.ID, "doubleClickMessage").click()
    assert self.driver.find_element(By.ID, "doubleClickMessage").text == "You have done a double click"
  
  def test_rightclick(self):
    self.driver.get("https://demoqa.com/buttons")
    self.driver.set_window_size(1294, 1392)
    button = self.driver.find_element(By.ID, "rightClickBtn")

    action_chains = ActionChains(self.driver)
    action_chains.context_click(button).perform()

    assert self.driver.find_element(By.ID, "rightClickMessage").text == "You have done a right click"

  def test_dynamicclick(self):
    self.driver.get("https://demoqa.com/buttons")
    self.driver.set_window_size(1294, 1392)
    self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/button").click()
    assert self.driver.find_element(By.ID, "dynamicClickMessage").text == "You have done a dynamic click"
