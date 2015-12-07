from pages.page import Page

class SauceMain(Page):
  """
  SauceMain class that represents the Sauce Labs main page
  """
  def find_pricing_link(self):
    return self.driver.find_element_by_link_text("PRICING")
    