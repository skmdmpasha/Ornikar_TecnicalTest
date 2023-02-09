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

[Root Directory] - Python_Bdd
        |---------------------- ConfigurationData
        |---------------------- [features]
                                    |--- environment.py
                                    |--- *.features
                                    |--- Pageobjects
                                            |----- _pages.py
                                    |----[steps]
                                            |----- _steps.py
        |---------------------- Logs
        |---------------------- resource
                                    |-------data
                                             |-- *{}.json
                                    |-------environment
                                             |---{}env.json
        |---------------------- [Utilities]
                                    |-------*.py

        |---------------------- [behave.ini | setup.cfg] (Optional Config Settings)

Configuration files (behave.ini, setup.cfg, tox.ini, and .behaverc) in Python Behave do not have problems like fixtures and can be used to setup the environment.

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

### Running program
# to execute all feature files (all tests)
behave features

# to execture specific feature
behave features/*.feature

# to see printed output add --no-capture
behave --no-capture

# run features with specific tags
behave --tags=without_login --tags=slow

```
# ----run with allure reports-------

# ----to run with allure reports please execute below command------
behave -f allure_behave.formatter:AllureFormatter -o reports/ features

# ------to view the reports------, 
allure serve reports/
```

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

Inspiration, code snippets, etc.

* [awesome-libraries](https://pypi.org/)

* [Python](https://www.python.org/)