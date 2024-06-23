# PySelAut

## Python Selenium Automation Framework!

### Features
- Page Object Model (check pages directory)
- Centralized locator repo (locators/locators.py)
- Passing env variables from command line (like browser=chrome, env=QA etc)
- Headless & headed execution (--headless=true|false)
- Passing test data file (--testdata=testdata/example_test_data.json)
- Cypress inspired simplified selenium api's such as visit(), type(), click() etc.

### Pre-requisite
- Python3

### Installation 
`pip install -r requirements.txt`

### How to run
```
pytest -srP --browser=chrome --headless=false --env=QA --login=standard_user --secret=secret_sauce --testdata=testdata/example_test_data.json tests/example_tests/example_test.py
```

### Allure Report integration (optional)

#### Pre-condition

1. Node.js should be installed
2. Java version 8 (jre is sufficient) and above should be installed & JAVA_HOME path should be set

refer https://allurereport.org/docs/install-for-nodejs/

Now install allure-commandline tools

`npx install allure-commandline`

- To generate allure reports along with pytest run tests like below, some additional file would be now generated in allure-report directory

```
pytest -srP --browser=chrome --headless=true --env=QA --login=standard_user --secret=secret_sauce --testdata=testdata/example_test_data.json tests/example_tests/example_test.py --alluredir=allure-report
```
- Run this command to convert allure-report into a htm file, this will generate 'html-report/index.html'

`npx allure generate --clean --single-file allure-report/ -o html-report`

- Run this command to view reports in browser

`npx allure serve allure-report/`



