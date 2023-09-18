### Project Description: Selenium Training Project
Who Is This Project For?
This project is ideal for:

Software testers and quality assurance professionals looking to enhance their Selenium skills.
Developers interested in automating web testing processes.
Anyone eager to explore web automation testing with Selenium.
## Getting Started
To get started with the Selenium Training Project, follow these steps:
- Prerequisites Git & Python3.11
- Create a Project Directory:
Create a new directory for your Selenium project where you'll organize your code and resources.
- Open terminal


Clone repo - 
```bash
git clone https://github.com/NataliaTester/demoQAtest.git
```

Go to project folder
```bash
cd demoQAtes
```

Create Virtual environment - 
```bash
python3 -m venv venv
```

Activate the virtual environment 
On Windows:- 
```bash
./venv/scripts/activate.ps1
```
On macOS and Linux:- 
```bash
source venv/bin/activate
```
Install Selenium:

```bash
pip install selenium
```

Download WebDriver Executable:

Selenium requires WebDriver executables for different browsers (e.g., Chrome, Firefox).Here are some common ones:
- Chrome WebDriver: https://sites.google.com/a/chromium.org/chromedriver/downloads
- Firefox WebDriver (GeckoDriver): https://github.com/mozilla/geckodriver/releases 

Place the WebDriver executable in a directory included in your system's PATH or specify its path in your Selenium code.

Run test scripts - 
```bash
py.test --browser_name=chrome -v -s
```
