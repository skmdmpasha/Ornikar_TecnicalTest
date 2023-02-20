# Project Title
Python_Bdd
Project intented to test Both API tests and UI tests

Simple overview of Both projects use/purpose.
API: https://dummy.restapiexample.com/
    BDD-style Rest API testing tool
    It uses python's requests for performing HTTP requests, 
    
    
UI: https://www.ornikar.com/
    Selenium Python Behave BDD & Selenium WebDriver

## Description
An in-depth view on automation project Structure and overview.

It uses python's requests for performing HTTP requests, nose for most assertions, trafaret for json validation and behave for BDD style of tests.
used nose for most assertions, trafaret for json validation and behave for BDD style of tests

To demonstrate the usage of Python Behave with local Selenium WebDriver, I’ll take the example of a       simple ornikar websitep.

You can see the snapshot of the project directory below, to be used in this Selenium Python framework.

## Project Structure
Feature files are intended to locate in /features folder

Corresponding steps are located in /features/steps

Overall project structure is as follows:

[Root Directory] - Python_Bdd/
```
+-- ConfigurationData
    +-- conf.ini  (store page locators.)

+-- requirements.txt // store python requirements

+-- Python_Bdd/

+-- features/

    +-- pageobjects // 

        +-- *.py // Python scripts related to corresponding feature (e.g. "login.py" contains steps that are related to "login.feature")

    +-- environment.py // context setup steps using HOOkS  (e.g. load from config)

    +-- *.feature // feature files

    +-- steps/

        +-- __init__.py // used to import predefined functions from Utilities

        +-- json_responses.py // response structures described in Trafaret format for schema validation

        +-- *.py // Gherkin steps related to corresponding feature (e.g. "login.py" containsgherkin  steps that are related to "login.feature")

+--- Logs

+--- resource
        +-- data
            +--*{}.json         (to store json templates...)(optional)

        +-- environment
            +-- {}env.json      To store project config (urls, global variables, etc.)

+--- [Utilities]
        +-- *.py    (helpers functions)

+--- [behave.ini | setup.cfg]   (Optional Config Settings)


Behave configuration files are known as the .behaverc/behave.ini/setup.cfg/tox.ini(any one and is set as per user choice).

Configuration files (behave.ini, setup.cfg, tox.ini, and .behaverc) in Python Behave do not have problems like fixtures and can be used to setup the environment.

I figured it out after spending more time reading the documentation. It is actually quite simple. By default, behave does not display any output (i.e. by using print()) unless there is a failure in the test. To force displaying all output regardless of the outcome of the test (pass/fail), all you need is to change some of the default settings. The easiest way to achieve that is to create a file named behave.ini in the root of your project's directory and put the following:

[behave]
stderr_capture=False
stdout_capture=False

Next time you run your behave tests, you will see all outputs from your debug statements whether your tests pass or fail.




## Getting Started
    Clone project

    Run pip install -r requirements.txt to install required dependencies

### Installing & setup env
    #-----environment creation--------
    $ python -m venv .venv

    # ---------activate environment----
    $ .\.venv\Scripts\Activate.ps1

### Dependencies
    # You can save the packages list to a separate file if you wanted to:
    $ pip freeze > requirements.txt

### CI reports
* ALLURE Reports

* Reports are generated into /reports folder
* Behave support JUnit reports, that are easily parsed by CI tools

# Running program


# ----run with allure reports-------

# ----to run all feature with allure reports please execute below command------

behave -f allure_behave.formatter:AllureFormatter -o allure_reports/ features

# ------to view the reports------, 
allure serve allure_reports/



# ---- to execute all feature files-----

behave features

# ---- to execture specific feature-----

behave features/*.feature

# ---- to see printed output add --no-capture -----

behave --no-capture

# ---- run features with specific tags-----

behave --tags=delete
behave features\api_user.feature --tags=delete



## Help

More about behave tool you can read here:
https://behave.readthedocs.io/
https://selenium-python.readthedocs.io/
```
command to run if program contains helper info
```
## Authors

Contributors names and contact info

* author : pasha SHAIK 
* email  : testeur.informatique@gmail.com

## Version History
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, downloads etc.

* [awesome-downloads](https://www.selenium.dev/downloads/)

* [awesome-libraries](https://pypi.org/)

* [Python](https://www.python.org/)