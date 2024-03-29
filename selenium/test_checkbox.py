from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions


class TestCheckbox():
  def setup_method(self, method):
    # Headless Chrome
    options = ChromeOptions()
    options.add_argument("--headless=new")
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
  
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_excel_checkbox(self):
    """Test case for excel checkbox"""
    self.driver.get("https://demoqa.com/checkbox")
    self.driver.set_window_size(1294, 1392)
    self.driver.find_element(By.XPATH, "//button[@title='Toggle']//*[name()='svg']").click()
    self.driver.find_element(By.XPATH, "//li[3]//span[1]//button[1]//*[name()='svg']").click()
    self.driver.find_element(By.XPATH, "//label[@for='tree-node-excelFile']//span[@class='rct-checkbox']//*[name()='svg']").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".text-success").text == "excelFile"
  
  def test_general_checkbox(self):
    """Test case for general checkbox"""
    self.driver.get("https://demoqa.com/checkbox")
    self.driver.set_window_size(1294, 1392)
    self.driver.find_element(By.XPATH, "//button[@title='Toggle']//*[name()='svg']").click()
    self.driver.find_element(By.XPATH, "//li[2]//span[1]//button[1]//*[name()='svg']").click()
    self.driver.find_element(By.XPATH, "//body//div[@id='app']//li[@class='rct-node rct-node-parent rct-node-expanded']//li[@class='rct-node rct-node-parent rct-node-expanded']//li[2]//span[1]//button[1]//*[name()='svg']").click()
    self.driver.find_element(By.XPATH, "//label[@for='tree-node-general']//span[@class='rct-checkbox']//*[name()='svg']").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".text-success").text == "general"