# Selenium Practice Automation

## Work in Progress: The development is ongoing. For updates, kindly revisit frequently.

### For this project, I used [https://demoqa.com/](https://demoqa.com/) website 

### In this folder, I created automation tests with Python, Selenium, Selenium IDE and Pytest to practice interaction with different elements in a web page. Every test interacts with an element from the webpage and checks if the interanction has been successful or not by asserting a specific condition.

---

### Continuous Integration/Continuous Deployment automation runs are configured in `ci.yml` file as follows:

* tests are running on push events
* test are running on schedule from Monday to Friday at 15:00 GMT (17:00 Brasov time)

### An HTML report is generated after each run and the last one can be vizualized on [https://costelburuiana.github.io/portofolio/?sort=result](https://costelburuiana.github.io/portofolio/?sort=result) or older reports can be downloaded in a .zip format from [https://github.com/costelburuiana/portofolio/actions](https://github.com/costelburuiana/portofolio/actions) and select the desired workflow run to see the report in `Artifacts` section of the page. 

---

### To run the tests, please follow these steps:

In `pytest.ini` file, the command line arguments for the tests are configured to run as default as follows:

* `-v` → more detailed information is displayed.
* `-rA` → shows a detailed summary of all tests except those that passed.
* `-s` → does not capture and will display outputs directly.
* `-n 20` → running the tests in 20 parallel processes to speed up the test run
* `--html=reports/index.html` → generates an HTML report. (name needs to be index.html for Github Pages)

All the tests are running in a virtual environment (pipenv). To run the tests, please follow these steps:

1. `pip install pipenv` → to install Pipenv on your local machine
2. `pipenv install` → the command will look for a Pipenv file. If it doesn’t exist, it will create a new environment and activate it. After the above command is run, we’ll find two new files: `Pipfile` and `Pipenv.lock`
3. `pipenv shell` → to activate already created pipenv environment
4. `pipenv install -r requirements.txt` → install dependencies from `requirements.txt`
5. `pytest` → to run all the tests as they are configured in `pytest.ini`

