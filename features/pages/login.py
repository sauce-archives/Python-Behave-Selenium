from pages.page import Page

class LoginPage(Page):
  """
  Login page of Saucedemo.com
  """
  def login_as_standard_user(self):
    self.driver.find_element_by_id('user-name').send_keys('standard_user')
    self.driver.find_element_by_id('password').send_keys('secret_sauce')
    self.driver.find_element_by_class_name('btn_action').click()

  def login_as_invalid_user(self):
    self.driver.find_element_by_id('user-name').send_keys('invalid')
    self.driver.find_element_by_id('password').send_keys('invalid')
    self.driver.find_element_by_class_name('btn_action').click()

  def is_error_displayed(self):
    return self.driver.find_element_by_class_name('error-button').is_displayed()



