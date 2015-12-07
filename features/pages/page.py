class Page(object):
  """
  Base class that all page models can inherit from
  """
  def __init__(self, selenium_driver):
    self.driver = selenium_driver
    
  def get_title(self):
    return self.driver.title

