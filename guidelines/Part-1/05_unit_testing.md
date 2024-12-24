# Unit testing our code 🧪

Welcome to the unit testing module! In this module, we'll explore the fundamentals of unit testing in Python using the pytest framework. Unit testing is a powerful tool to ensure that individual components of your code work as intended, and it's an integral part of a robust development process. By the end of this module, you'll be equipped with the knowledge to write effective unit tests for your Python code, leading to more reliable and maintainable software. Here are the concepts that we will cover:


- [Section 1: Unit tests](#section-1-unit-tests)
  - [Setting Up Pytest](#setting-up-pytest)
  - [Introduction to Unit Testing](#introduction-to-unit-testing)
  - [Organizing Test Cases](#organizing-test-cases)
  - [Testing with DataFrames](#testing-with-dataframes)
  - [Test for Exceptions](#test-for-exceptions)
  - [Parameterized Testing](#parameterized-testing)
- [Section 2: Test Coverage](#section-2-test-coverage)
  - [Installing pytest-cov](#installing-pytest-cov)
  - [Running the Coverage Test](#running-the-coverage-test)
- [Exercises](#exercises)
    - [✅ Module validation](#✅-module-validation)


## Section 1: Unit tests
### Introduction to Unit testing
Unit testing is an essential practice in software development that involves testing parts of code like functions or methods in isolation to ensure they work as expected

Unit testing is important to:
- Ensures code reliability by catching bugs early.
- Facilitates refactoring with confidence, knowing changes won’t break existing functionality.
- Encourages modular code design and better documentation.


### Testing with Pytest
Pytest is a popular testing framework in Python that simplifies the creation and execution of unit tests. Its key strength lies in its simplicity, making it easy to write small, readable test cases while still offering the scalability needed for larger and more complex projects.

Pytest supports features such as fixtures, parameterized testing, and detailed reporting, which we will detail in this module. It also integrates smoothly with continuous integration workflows, making it an ideal choice for automated testing in CI/CD pipelines.

By adopting Pytest, developers can improve code quality, catch bugs early, and write more maintainable code through thorough test coverage.

### Setting Up Pytest:
There are many libraries in python that will help with testing but a favourable one is called pytest.
To begin unit testing with pytest, you need to set up the framework in your development environment. Follow these steps to install pytest for use in your project:

  1. Installation:
     Use pip to install the pytest package. Run the following command in your terminal:
     ```bash
     pip install pytest
     ```

  2. Verify Installation:
     Confirm that pytest has been installed correctly by running the following command:
     ```bash
     pytest --version
     ```
     This should display the installed version of pytest.



### Pytest basic usage
A unit test in pytest is a function that calls another function and uses assertions to validate the behavior.

Assertions play a critical role in unit testing. They are used to confirm that the code under test behaves as anticipated. In pytest, the `assert` keyword is used to perform these checks. When pytest encounters an `assert` statement, it evaluates the associated expression, which should be `True`. If the expression evaluates to `False`, pytest raises an `AssertionError`, indicating that the test has failed.

Here's a simple example of a unit test:
```python
def test_addition():
    assert 1 + 1 == 2, "Test failed, 1 + 1 should equal 2"

def test_subtraction():
    assert 2 - 1 == 1, "Test failed, 2 - 1 should equal 1"
```

Here's an example of a unit testing a function:
Let's assume that we have a function called multiply_by_two which takes an integer and multiply it by 2

```python
from lib.preprocessing import my_function

def test_my_function():
    assert multiply_by_two(6) == 2, "Test failed, multiply_by_two(6) should return 12"
```


### Organizing Test Cases:

To ensure Pytest can find and run your tests while keeping your test suite organized, follow these best practices:

1.	Create a tests Directory
To maintain a clean and organized project structure, create a dedicated `tests` directory at the root of your project. This ensures that all test files are centralized and easy to manage.

2.	Name Test Files Clearly
Use a consistent naming convention for test files by prefixing them with `test_` (e.g., `test_module.py`). This helps Pytest automatically identify and run these files. The `test_` prefix is crucial for Pytest to recognize the file as containing test cases.

3.	Organize Tests by Functionality
Structure your test files to mirror your project’s module structure. For example, if you have a `module.py`, you can create a corresponding `test_module.py` to keep related tests and code organized.

4. Add `conftest.py` to your tests directory. `conftest.py` file is used to define fixtures and configuration options that can be shared across multiple test files in a project. We will detail fixtures later in this module

Your project structure should look something like this:
```
project/
├── bin/
├── lib/
│   ├── data_loading.py
│   └── preprocessing.py
├── notebooks/
├── tests/
│   ├── conftest.py
│   ├── test_data_loading.py
│   └── test_preprocessing.py
```

5.	Write Test Cases
Within each test file, write individual test functions prefixed with `test_` (e.g., `test_functionality()`). This makes it easy for Pytest to detect and execute them. Each test function should focus on a single unit of functionality to ensure precise testing and better readability.

6.	Run Your Tests
After writing your test cases, simply run `pytest` in your terminal. Pytest will automatically discover and execute all test files and functions in the tests directory, ensuring that your entire test suite runs seamlessly.



### Testing with DataFrames:
Testing with Pandas DataFrames in pytest may require special considerations, we should use  Pandas’ built-in testing utilities, such as assert_frame_equal, which handle these intricacies.

Here’s an example:
```python
import pandas as pd
import pandas.testing as pdt

def test_dataframe_equality():
    # Sample DataFrames for testing
    df1 = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    df2 = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

    # Use pandas.testing to ensure DataFrame equality
    pdt.assert_frame_equal(df1, df2)
```

`pandas.testing.assert_frame_equal()` compares two DataFrames considering data types, index/column order, and NaN handling. This method provides meaningful error messages when the DataFrames differ, making it easier to debug failing tests.

For comparing Pandas Series objects, we use the function `pandas.testing.assert_series_equal()`.



### Test for Exceptions:
In pytest, it’s crucial to verify not only the successful execution of code but also that certain errors are properly handled by raising expected exceptions. This ensures your code behaves predictably when encountering error conditions. You can use pytest.raises() to test for exceptions.

Here’s an example:
```python
import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
```

In this example, pytest.raises() checks if the divide() function raises a ValueError with the correct error message when dividing by zero. This helps ensure that your code handles edge cases and errors in a controlled and predictable way.



### Parameterized Testing:
Parameterized testing allows you to run the same test function with different sets of arguments, ensuring that the function is tested against a variety of inputs. In pytest, this can be easily achieved using the @pytest.mark.parametrize decorator.

With `@pytest.mark.parametrize`, you define the set of parameters you want to test and pass them to the function as arguments. This allows for more comprehensive testing with less repetitive code.

```python
import pytest

@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 4),
    (3, 6),
    (4, 8)
])
def test_double(input, expected):
    assert input * 2 == expected
```

In this example, the test_double function will be run four times, each time with a different combination of input and expected values. If any assertion fails, pytest will report which specific input combination caused the failure.

This approach is especially useful when testing functions that need to handle a wide range of inputs or edge cases.


### Fixtures and mocks
Sometimes, you may need to run the same line of codes in multiple tests, whether it is loading a dataset or initiate an object of a specific class. As it may become really repetitive to write those same lines of code over and over, it would be much nicer to do it once and for all your tests. That’s what fixture are for !

Fixtures allow you to use the output of a specific function as a variable for all of your tests. The actual function only need to be written once, and can be used directly by specifying it as argument in your test.

```python
@pytest.fixture
def mocked_dataframe():
    return pd.DataFrame({"some_column": ["some", "data"]})

def test_is_dataset_not_empty(mocked_dataframe):
    assert is_dataset_not_empty(mocked_dataframe)
```

Some fixtures may even be useful for a lot of tests, that are not necessarily in the same file. To avoid writing the same fixture in each test file, you can directly write them in a conftest.py file. When running a test, pytest will automatically check on fixtures defined in conftest.py, and import them in all your tests files so you can directly import them as variable.

Using previous example, we could just have a conftest.py file where mocked_dataframe is defined, and use it in our test_is_dataset_empty function by specifying it as an argument.

Example of a `conftest.py`:
```python
import pytest
import pandas as pd

@pytest.fixture
def mocked_dataframe():
    return pd.DataFrame({"some_column": ["some", "data"]})
```

And we can use this `mocked_dataframe` ficture in our test files without even importing it

### Mocks
More generally, a mock is an object made for impersonating another one during a test, to avoid calling the actual object. Like every objects, it has a unique instance id, meaning two mocks are completely different objects.

The best and easiest way to define mocks is to use MagicMock.

MagicMock allows you to easily create a mock for every type of object, with a unique instance id. Two mocks therefore are completely different objects.


Here's an example of using `MagicMock` to mock a database connection in a test:
```python
from unittest.mock import MagicMock
import pytest
# Function that uses a database connection
def function_under_test(db_connection):
    return db_connection.query("SELECT FROM users")

# Test function
def test_function_under_test():
    # Create a mock object for the database connection
    mock_db_connection = MagicMock()

    # Set up the mock to return a specific value when query is called
    mock_db_connection.query.return_value = "mocked result"

    # Call the function under test with the mock object
    result = function_under_test(mock_db_connection)

    # Assert that the function returned the mocked result
    assert result == "mocked result"
```



## Section 2: Test Coverage

Testing coverage is an important aspect of software development, as it measures the extent to which your codebase is tested by automated tests. It helps identify untested parts of the code, ensuring better reliability and maintainability. `pytest` is a powerful testing framework for Python that can be extended with plugins like `pytest-cov`, which provides an easy way to measure code coverage while running your tests.

While test coverage is beneficial for ensuring code quality in traditional software, it’s not mandatory in ML products due to their heavy reliance on data. Testing in ML should focus on data validation and model performance, as high code coverage alone doesn’t guarantee model accuracy or robustness.

### Installing pytest-cov
To use pytest-cov, you need to install the plugin alongside pytest. You can do this using pip. Here’s how to install it after installing pytest:
```bash
pip install pytest pytest-cov
```



### Running the Coverage Test
Once you have installed pytest-cov, you can run your tests with coverage tracking enabled. Use the following command in your terminal:

```bash
pytest --cov=my_directory
```

- --cov=lib: This flag tells pytest to calculate the coverage for the `my_directory` directory. Code coverage measures how much of your code is executed while the tests are running.

Here are other flags that could be interesting

- -s: This flag disables the capturing of standard output (stdout). By default, pytest captures the output of the tests and prints it only for failing tests. Using -s allows you to see the output for all tests, which can be useful for debugging.

- -vv: This increases the verbosity of the test output. pytest has several verbosity levels, and -vv provides more detailed information about the tests being run.``

- --cov-report=term-missing: This option specifies the type of coverage report to generate. In this case, it tells pytest-cov to output the coverage report to the terminal and to list the lines that are not covered by tests (missing coverage).

- --cov-fail-under=20: This sets a minimum threshold for test coverage percentage. If the total coverage percentage is below 20%, pytest will exit with a failure status. This is a way to enforce a certain level of code coverage in your project.



## Exercises

### ✅ Module validation
1. Create a new branch named `feat/unit-tests`.
2. Create a `tests` directory at the root of the project
3. Install pytest and pytest-cov
4. Create tests for these preprocessing functions:
    - drop_cols (one for functionality and one for KeyError - Don't forget to parametrize your tests)
    - create_target (one for functionality and one for KeyError - Don't forget to parametrize your tests)
5. Include your tests in the CI
6. Create a pull request to merge `feat/unit-tests` into the main branch.
7. Merge the pull request on GitHub.


Thanks for completing this module on unit testing! 🎉 In the [next module](./06_code_documentation), we’ll explore the best practices for documenting our code to make it clear, maintainable, and accessible.
