from pages.page import Page

class InventoryPage(Page):
  """
  Inventory page of Saucedemo.com
  """
  def add_item(self):
    self.driver.find_element_by_class_name('btn_primary').click()

  def remove_item(self):
    self.driver.find_element_by_class_name('btn_secondary').click()

  def get_cart_items(self):
    return self.driver.find_element_by_class_name('shopping_cart_badge').text

