import os
from selenium import webdriver

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')


def make_browser(name):
  desired_cap = {
      "name": name,
      "platform": os.environ.get('platform'),
      "browser_name": os.environ.get('browserName'),
      "version": os.environ.get('version'),
      "build": "Sample Behave",
  }
  browser = webdriver.Remote(
  command_executor ='http://{}:{}@ondemand.saucelabs.com:80/wd/hub'.format(username, access_key),
  desired_capabilities = desired_cap)
  return browser







