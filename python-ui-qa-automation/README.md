####Python UI Automation Framework (PyTest + Selenium)

This project is a UI automation framework built using **Python**, **PyTest**, and **Selenium WebDriver**.  
It follows the **Page Object Model (POM)** design pattern and supports:

- PyTest Fixtures  
- Logging  
- Headless Execution  
- JSON Test Data  
- GitLab CI/CD Integration  
- Page Objects for Test Scalability  

## Project Structure**
project/
│
├── allure-results/          # Raw data (JSON, screenshots)
├── allure-report/           # Generated HTML report
├── tests/
├── pageObjects/
├── utilities/
├── conftest.py
├── pytest.ini
└── requirements.txt


## Project Structure**
python-ui-qa-automation/
│
├── .venv/ or .venv1/           # Virtual environment
├── logs/                       # Auto-generated logs
│
├── pageObjects/
│   ├── HomePage.py             # Page class for Automation Practice site
│   ├── LoginPage.py            # Page class for Login
│   └── __init__.py
│
├── test_data/
│   └── test_data.json          # Test input values
│
├── tests/
│   ├── test_e2e.py             # Main test file
│   └── __init__.py
│
├── utilities/
│   ├── BaseClass.py            # Common utilities (scroll, wait, logger)
│   ├── logger.py               # Logger implementation
│   ├── conftest.py             # PyTest fixtures (browser setup, login)
│   └── __init__.py
│
├── requirements.txt            # Python dependencies
└── README.md                   # Framework documentation

## Install Dependencies
pip install -r requirements.txt

## Run all tests
pytest -v -s <test_file_name>

## Generate HTML report:
allure generate allure-results -o allure-report --clean

## View report:
allure serve allure-results