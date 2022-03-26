# hudl-tech-test

## Setup

I setup the test framework using Page Object Model. They advantages of using POM are;

- Makes our code cleaner and easy to understand.
- Tests are more readable, flexible, and maintainable.
- Re-usable code that reduces redundancy of code.
- Shorten the learning curve for testers and help QA teams meet timelines.

### Test cases
I won't be covering a lot of negative test cases as this will bloat the E2E tests. I believe negative test cases should be covered on the lower level such as unit and API level, UI tests should focus on the happy paths and critical flows. Below are the list of test cases I will be writing;
- Login with valid credentials
- Login with invalid credentials and verify the error message
- Login with missing credentials (email or password) and verify the error message

### Drivers

Drivers can be set in system path on your local machine, but for this project I have put all drivers inside `drivers` director and I only used Chrome and Firefox drivers, but other drivers such as IE, Safari can be used. Please note that you need to have the browser of the driver you instead to use installed on your local machine.

- In case the `chromedriver` doesn't work, please download the chromedriver version that correlates with the same version of your Chrome browser and swap it for this one.

### Packages

In order to install the packages used for this project, please create a virtual env by following these steps.

#### Installing virtualenv

First of all, you need to install `virtualenv` if you haven't before. If you are using a `Unix/macOS` use this command `python3 -m pip install --user virtualenv` and for `Windows` use this command `py -m pip install --user virtualenv`

#### Creating a virtual environment

Next we need to create a virtual env inside our directory. For `Unix/macOS` use this command `python3 -m venv env` and for `Windows` use this command `py -m venv env`

#### Activating a virtual environment

Before you can start installing or using packages in your virtual environment you’ll need to activate it. To do so, for `Unix/macOS` run `source env/bin/activate` and for `Windows` use this command `.\env\Scripts\activate`

**Side note** to leave a a virtual enviromment, just run `deactivate` inside the directory.

#### Installing packages

Arghhhh the final step! To install the needed packages for this project, which can be loacted inside the `requirements.txt` please run the following command for `Unix/macOS` use `python3 -m pip install -r requirements.txt` and for `Windows` use this command `py -m pip install -r requirements.txt`

### Run Tests

To run tests please make sure you have an activated env with all the need ackages from `requirements.txt`already installed.
The command for running the test is `pytest tests --browser [browsername]` for example, say you want to run your test on a chrome browser `pytest tests --browser chrome` or on firefox then use this command `pytest tests --browser firefox`.

### Test Report

For test resport I am keeping it simple by using `pytest-html`. Run the following command to run tests and save html report on the root of the directory `pytest -v tests --browser chrome --html=htmlreport.html `
