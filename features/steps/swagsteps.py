from selenium import webdriver
from pages.login import LoginPage
from pages.inventory import InventoryPage
from features.browser.browsers import make_browser

@given('we are on a browser')
def start_browser(context):
  context.browser = make_browser(context.name)

@given('we are on the swag labs site')
def step_impl(context):
  context.browser.get('http://www.saucedemo.com')
  context.login = LoginPage(context.browser)

@when('we login as a standard user')
def step_impl(context):
  context.login.login_as_standard_user()

@then('we should be on the inventory page')
def step_impl(context):
  assert "Swag" in context.login.driver.title

@when('we login as an invalid user')
def step_impl(context):
  context.login.login_as_invalid_user()

@then('it should raise an error')
def step_impl(context):
  assert context.login.is_error_displayed()

@given('we are on the inventory page')
def step_impl(context):
  context.browser.get('http://www.saucedemo.com/inventory.html')
  context.inventory = InventoryPage(context.browser)

@when('we add an item to the cart')
def step_impl(context):
  context.inventory.add_item()

@when('we add two items to the cart')
def step_impl(context):
  context.inventory.add_item()
  context.inventory.add_item()

@then('we should see one item in our cart')
def step_impl(context):
  assert context.inventory.get_cart_items() == '1'

@then('we should see two items in our cart')
def step_impl(context):
  assert context.inventory.get_cart_items() == '2'