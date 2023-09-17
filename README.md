# Project Workflow:
## Prerequisites Git & Python3.11


Open terminal

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

Enter the virtual environment - 
```bash
./venv/scripts/activate.ps1
```

Install packages - 
```bash
pip3 install -r requirements.txt
```

Run test scripts - 
```bash
py.test --browser_name=chrome -v -s
```