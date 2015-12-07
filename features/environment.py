import os
from sauceclient import SauceClient
from features.browser.browsers import username, access_key

def before_scenario(context, scenario):
  context.name = scenario.name

def after_scenario(context, scenario):
  if hasattr(context, 'browser'):
    context.browser.quit()
    sauce_client = SauceClient(username, access_key)
    passed = scenario.status == 'passed'
    sauce_client.jobs.update_job(context.browser.session_id, passed = passed)
    