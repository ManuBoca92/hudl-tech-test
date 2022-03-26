# hudl-tech-test

### Test cases

- Login with valid credentials
- Login with invalid credentials and verify the error message
- Login with missing credentials and verify the error message

## Setup

I will using Page Object Model to setup the test framework. They advantages of using POM are;

- Makes our code cleaner and easy to understand.
- Tests are more readable, flexible, and maintainable.
- Re-usable code that reduces redundancy of code.
- Shorten the learning curve for teststa nd help QA teams meet timelines.

### Drivers

Drivers can be set in system path for this project I have put all drivers inside `drivers` directory. For this project I used Chrome and Firefox drivers but other drivers for IE, Safari can be used. Please note that you need to have the browser of the driver you instead to use installed on your local machine.

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

### Test Report

For test resport I am keeping it simple by using `pytest-html`. Run the following command to run tests and save html report on the root of teh directory `pytest -v tests --browser chrome --html=htmlreport.html `
