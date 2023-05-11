# Test Framework

Test Framework is a Python-based automation testing framework for web applications using pytest.

## Installation

Before you can start using this framework, you need to install the following dependencies:

* Python 3.7 or later
* pip

Additionally, you need to clone the repository to your local machine:

git clone https://github.com/Pavlenkovv/Test_Framework.git

cd Test_Framework
pip install -r requirements.txt


## Usage

To run tests, execute the following command in your terminal:

pytest


This command will discover all tests in the `tests` directory and run them.

## Writing Tests

Tests in Test Framework are written using pytest. Here is an example test:

```python
def test_login():
    # Your test code here
    assert True
