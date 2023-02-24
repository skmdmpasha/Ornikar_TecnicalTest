from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# from selenium.common import exceptions
# from selenium.webdriver.common import desired_capabilities
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait

from Utilities import configReader, helperFunctions
# ***************************************************************
import yaml
import allure
import json
import os
from yaml import *
import features.steps.json_responses as json_responses


def before_all(context):

    # ********************Browser reading****************************
    context.browser_CMDParam = context.config.userdata.get("BROWSER")
    context.browser_name = configReader.readConfig("basic info", "browser")
    context.browser_url = configReader.readConfig("basic info", "test_site_url")
    # ***************************************************************

    print_star = ''.join('*' for i in range(len('before_all')))
    print(print_star+' Hook before_all '+print_star)
    # context.settings = yaml.load(open('features/conf.yaml').read(),  Loader=yaml.FullLoader)
    context.settings = yaml.load(
        open('resource/environment/env.json').read(),  Loader=yaml.FullLoader)
    context.staging_url = context.settings['staging']
    context.base_url = ""
    context.headers = {
        'Content-Type': 'application/json', 'User-Agent': 'request'}

    context.json_responses = json_responses

    # SSL validation
    context.verify_ssl = True
    # By default, requests has a turned on SSL validation.
    # This can be turned off globally, by setting context.verify_ssl = True in environment.py


def before_feature(context, feature):
    if 'UI' in feature.tags:
        if context.browser_name!='':
            browser_name = context.browser_name
        if context.browser_CMDParam != None:
            browser_name = context.browser_CMDParam
            print(f"Taken {browser_name} from commandline...")
        if context.browser_name=='' and context.browser_CMDParam==None:
            browser_name = os.environ.get('BROWSER', 'firefox')
            print(f"Taken {browser_name} as Defualt Browser...")
        
        if browser_name == "chrome":
            options = helperFunctions.set_browser_options("chrome")
            context.driver = webdriver.Chrome(
                ChromeDriverManager().install(), options=options)
        elif browser_name == "firefox":
            options = helperFunctions.set_browser_options("firefox")
            context.driver = webdriver.Firefox(service=Service(
                GeckoDriverManager().install()), options=options)
        elif browser_name == "chromium":
            context.driver = webdriver.Chrome(ChromeDriverManager(
                chrome_type=ChromeType.CHROMIUM).install())
        elif browser_name == "brave":
            context.driver = webdriver.Chrome(
                ChromeDriverManager(chrome_type=ChromeType.BRAVE).install())
        elif browser_name == "ie":
            context.driver = webdriver.Ie(IEDriverManager().install())
        elif browser_name == "edge":
            context.driver = webdriver.Edge(
                EdgeChromiumDriverManager().install())

        # launch application Ornikar
        context.driver.maximize_window()
        helperFunctions.launchBrowser(context, context.browser_url)
    # else:
    #     raise ValueError(f'Invalid browser name: {browser_name}')


def after_feature(context, feature):
    print()
    if 'UI' in feature.tags:
        context.driver.quit()


def before_step(context, step):
    print('\n\n')


def after_step(context, step):
    print('\n\n')
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

# def after_scenario(context, driver):
#     context.driver.quit()


def before_scenario(context, scenario):
    print(scenario.keyword)
    context.scenario = scenario
    print()
    # if context.failed == True:
    #     print(context.scenario, 'failed. Here are the tags:')
    #     for tag in context.tags:
    #         print(tag)
