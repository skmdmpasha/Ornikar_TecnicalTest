from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Utilities import configReader, helperFunctions
# ***************************************************************
import yaml
import allure
import json
from yaml import *
import features.steps.json_responses as json_responses


def before_all(context):
    print_star=''.join('*' for i in range(len('before_all')))
    print(print_star+' Hook before_all '+print_star)
    # context.settings = yaml.load(open('features/conf.yaml').read(),  Loader=yaml.FullLoader)
    context.settings = yaml.load(open('resource/environment/env.json').read(),  Loader=yaml.FullLoader)
    context.staging_url = context.settings['staging']
    context.base_url = ""
    context.headers ={'Content-Type': 'application/json', 'User-Agent': 'request'}
    context.json_responses = json_responses
    
    # SSL validation
    context.verify_ssl = True
    # By default, requests has a turned on SSL validation. 
    # This can be turned off globally, by setting context.verify_ssl = True in environment.py

def before_feature(context, feature):
    env_name = 'staging'

    # ALL available browser drivers
    if 'UI' in feature.tags:
        if configReader.readConfig("basic info","browser")=="chrome":
            options=helperFunctions.set_browser_options("chrome")
            context.driver=webdriver.Chrome(ChromeDriverManager().install(), options=options)
        elif configReader.readConfig("basic info","browser")=="firefox":
            options = helperFunctions.set_browser_options("firefox")
            context.driver=webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()), options=options)
        elif configReader.readConfig("basic info","browser")=="chromium":
            context.driver=webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
        elif configReader.readConfig("basic info","browser")=="brave":
            context.driver=webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install())
        elif configReader.readConfig("basic info","browser")=="ie":
            context.driver=webdriver.Ie(IEDriverManager().install())
        elif configReader.readConfig("basic info","browser")=="edge":
            context.driver=webdriver.Edge(EdgeChromiumDriverManager().install())
        
        # # lauch application ornikar
        helperFunctions.launchBrowser(context, configReader.readConfig("basic info","testsiteurl"))

def after_feature(context, feature):
    if 'UI' in feature.tags:
        context.driver.quit()

def after_step(context, step):
    print()
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)


# def after_scenario(context, driver):
#     context.driver.quit()

# def after_scenario(context, scenario):
#     if context.failed == True:
#         print(context.scenario, 'failed. Here are the tags:')
#         for tag in context.tags:
#             print(tag)
