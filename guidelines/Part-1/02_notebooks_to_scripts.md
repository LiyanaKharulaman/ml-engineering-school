# Convert Notebooks to Scripts 💻

In this module, you will learn how to transform your Jupyter notebooks into standalone Python scripts. This process will enable you to run your code outside the Jupyter environment, facilitating automation and integration into larger projects. Here are the concepts that we will cover:

- [Section 1: Functions and Modules](#section-1-functions-and-modules)
  - [Modules](#modules)
  - [Classes vs Functions](#classes-vs-functions)
  - [Designing Specialized Functions](#designing-specialized-functions)
  - [Function Naming Best Practices](#function-naming-best-practices)
  - [Types and Return Type](#types-and-return-type)
- [Section 2: Scripts and Command Line Interfaces](#section-2-scripts-and-command-line-interfaces)
  - [Main.py](#mainpy)
  - [Passing arguments to scripts](#passing-arguments-to-scripts)
  - [The Main Guard in Python](#the-main-guard-in-python)
  - [Shell Scripts for running Python script Efficiently](#shell-scripts-for-running-python-script-efficiently)
- [Exercises](#exercises)
    - [✅ Module Validation](#✅-module-validation)

## Section 1: Functions and modules

### Modules
In Python, a module is essentially a single file (with a .py extension) that contains Python code. Modules allow for better code organization by grouping related functions, classes, and variables into one file. By breaking down a project into smaller, reusable modules, the code becomes more maintainable and scalable.

Each module can contain multiple functions that perform specific tasks, allowing for a modular approach to development. Once a module is created, it can be imported and reused across different Python scripts or even by other modules. This promotes code reusability and avoids duplication.

To use a function form a module in Python, you simply import it using the import statement.

Here's an example:
```python
from lib.plots import plot_correlation_heatmap

fig = plot_correlation_heatmap(df, ["Age", "Bonus", "Poldur", "Value"])
fig.show()
```

### Classes vs Functions
In Python, both functions and classes are fundamental programming constructs, but they serve different purposes:

1. **Functions** are blocks of code that perform a specific task and can be reused. They take inputs (parameters), perform an action, and return output (if any).
2. **Classes** define objects, which are more complex structures that encapsulate both data (attributes) and methods (functions that operate on the data).

**When to use Functions**:
- Use when you have a simple task to accomplish.
- Use if you need something quick and stateless (without needing to maintain or manipulate data over time).

**When to use Classes**:
- Use when you need to represent something more complex with both data (attributes) and behavior (methods).
- Use when you want to create reusable blueprints (objects) that can manage internal states (like configuration).


**Example of sklearn model class**:
In the sklearn library, models are implemented as classes. This allows you to create an instance of a model, configure it, train it on data, and then use it to make predictions, all while maintaining the model’s internal state (like learned parameters).

```python
# Import the LinearRegression class
from sklearn.linear_model import LinearRegression

# Create an instance of the LinearRegression class (object creation)
model = LinearRegression()

X = ...
y = ...

# Train the model (fit method)
model.fit(X, y)
```

Class (LinearRegression): The LinearRegression class encapsulates methods and attributes related to the linear regression model.
- Attributes: Holds things like coefficients, intercept, etc., after the model is trained.
- Methods: Such as fit() to train the model and predict() to make predictions.

Note: While this module does not require you to create classes, understanding their structure and purpose is very important.


### Designing specialized functions

A well-designed function should have a distinct purpose and execute a single, focused task. This approach simplifies the function's comprehension, facilitates its testing, and enhances its maintainability. Additionally, it encourages code reuse, as the function can be applied in various sections of the project.

Here's an example of a function whose sole purpose is to plot a correlation heatmap:
```python
def plot_correlation_heatmap(df, numerical_features):
    corr = df[numerical_features].corr()
    fig = go.Figure(data=go.Heatmap(z=corr.values, x=corr.columns, y=corr.columns, colorscale="Viridis"))
    fig.update_layout(title="Correlation Heatmap for Numerical Features")
    return fig
```

If a function is found to perform multiple tasks, it is advisable to refactor it into separate, specialized functions.


### Function naming best practices

When naming functions, it's essential to follow best practices to ensure that the names are clear, concise, and descriptive. Here are some guidelines to keep in mind:

* **Use descriptive names**: Choose names that accurately describe what the function does. For example, `download_data` is a better name than `fetch_data`.
* **Use verbs**: Function names should typically start with a verb, indicating the action the function performs. For example, `read_data` or `process_input`.
* **Avoid ambiguity**: Ensure that the name does not have multiple meanings or interpretations. For example, `calculate` is too generic; `calculate_metrics` is more specific and clear.
* **Keep it concise**: Aim for a balance between brevity and clarity. Avoid using overly long names, but ensure they are still descriptive.

Here's an example of a well-named function:
```python
def preprocess_data(df):
    # Function implementation
    pass
```
In this example, the function name `preprocess_data` clearly indicates that it processes data in some way.


### Types and return type

When writing functions, it's essential to specify the types of the function's parameters and its return value. This is known as type hinting. Type hinting helps in several ways:

* It makes the code more readable by explicitly indicating the expected types of parameters and the return value.
* It allows for static type checking, which can catch type-related errors before the code is even executed.
* It provides better auto-completion and documentation for other developers working on the project.

Here's an example of a function with type hinting:
```python
def my_function(var1: str, var2: pd.DataFrame, var3: int = 0) -> list[str]:
    # Function implementation
    pass
```
In this example, `var1` is expected to be a string, `var2` is expected to be a pandas DataFrame, and `var3` is an optional integer with a default value of 0. The function returns a list of strings.


## Section 2: Scripts and Command Line Interfaces

When it comes to putting code into production, scripts are the preferred choice over notebooks. They offer better code organization, easier debugging, and improved performance. Additionally, scripts can be easily version-controlled, making it simpler to track changes and collaborate with others.


### Main.py
The main.py file typically serves as the entry point for a Python application. Its main role is to organize the execution flow of the program by calling the appropriate functions or classes. The key principles behind main.py include:


To run the main.py file, assuming you’re in the root directory of the project:
```python
python main.py
```

### Passing arguments to scripts

Now, we’ll explore how to pass arguments to a script. A Command Line Interface (CLI) is a way for users to interact with software applications by typing commands into a terminal or command prompt. This process of passing arguments to a script is an essential aspect of creating a CLI. To handle command-line arguments effectively in Python, we commonly use tools like `argparse`.

**Argparse**:<br>

Argparse is a Python module that makes it easy to write user-friendly command-line interfaces. It can parse the arguments passed to the script and convert them into Python objects. Here's a simple example of how to use Argparse:

```python
import argparse

parser = argparse.ArgumentParser(description='Description of your script')
parser.add_argument('--param1', type=int, help='Description of param1')
parser.add_argument('--param2', type=str, help='Description of param2')
args = parser.parse_args()
params = vars(args)

# Main python code
...
```

In this example, we create an ArgumentParser object and add two arguments to it. The `parse_args` method then parses the arguments and returns them as a namespace. We convert this namespace to a dictionary using the `vars` function.

Note: No need to install `argparse` separately if you have Python as it is included in it.


**Other CLI Tools**: <br>

After discussing argparse, we can introduce two powerful libraries for building more complex CLIs:

1.	Typer: This library simplifies the creation of command-line interfaces by leveraging Python’s type hints. Typer makes it easy to create sophisticated CLIs with minimal boilerplate code. (See more here: https://typer.tiangolo.com/)
2.	Fire: Fire is another library that allows you to generate a CLI from a Python function quickly. With Fire, you can expose functions as CLI commands with just a few lines of code, making it a great tool for rapid development. (See more here https://github.com/google/python-fire)

By using Typer and Fire, you can enhance the usability and functionality of your scripts significantly.


### The Main Guard in Python

You have likely encountered `if __name__ == "__main__"` but what does it do?

The `if __name__ == "__main__":` construct in Python also known as the 'main guard' is used to check whether a script is being run directly or imported as a module. When the script is executed directly, the `__name__` variable is set to `"__main__"`, and the code inside the if block runs. If the script is imported into another module, the `__name__` variable will have the module’s name, and the code inside the block won’t execute.

This pattern is useful to prevent certain code (like test cases or script-specific logic) from running when the script is imported elsewhere.


### Shell Scripts for running Python script Efficiently

When running Python scripts from the command line, it's a good practice to use shell scripts. These scripts can be placed in a `bin` folder for easy access.

Here's an example of a shell script to run a Python script with default parameters:
```bash
#!/bin/bash
# Run the Python script with arguments
python my_script.py --param1 value1 --param2 value2
```

Here's how you can set default values
```bash
#!/bin/bash
# Set default values
PARAM_1=5
PARAM_2=10

# Run the Python script with arguments
python my_script.py --param1 $PARAM_1 --param2 $PARAM_2
```

If you want to request user input for a parameter, you can use the `read` command in the shell script:
```bash
#!/bin/bash
# Set default values
PARAM_1=5
PARAM_2=10

# Ask for user input otherwise take default value
read -p "Enter param1 (default: $PARAM_1): " user_param_1
PARAM_1=${user_param_1:-$PARAM_1}

read -p "Enter param2 (default: $PARAM_2): " user_param_2
PARAM_2=${user_param_2:-$PARAM_2}

python my_script.py --param1 $PARAM_1 --param2 $PARAM_2
```

Remember to make the shell script executable before running it using the `chmod` command:
```bash
chmod +x my_script.sh
```


## Exercises

### ✅ Module validation

1. Create a new branch named `feat/notebooks-to-scripts`.
2. Create Scripts:<br>
    Create separate Python scripts in `/lib` for each step.
    - data_loading.py
    - preprocessing_py
    - modelling.py
    - evaluation.py
3. Modularize the Code:<br>
    Within each script, modularize your code into functions. This will make your code more readable and reusable. Make sure to follow naming best practices and use type hints for your function arguments and return values.
    Here are the expected functions:
    - data_loading.py
        - download_data
        - read_data
    - preprocessing.py
        - create_target
        - drop_cols
        - preprocess_data
        - split_data
    - modelling.py
        - init_preprocessor
        - init_pipeline
        - train_pipeline (which will init the pipeline and fit it to the training data)
    - evaluation.py
        - calculate_metrics
4. Refactor your notebook:<br>
    Refactor your Jupyter notebook to call these functions instead of having the code directly in the notebook. This will make your notebook more concise and easier to understand.
    To ensure your notebook can locate the scripts, consider adding the following code at the beginning of your notebook:
    ```
    import sys

    sys.path.append("../")
    ```
5. Add Main.py:<br>
    - Create a new Python script named `main.py`, that will run your ML code in the main guard `if __name__ == "__main__"`
    - Adapt your script to accept the following arguments: `n_estimators`, `learning_rate` and `max_depth`. We recommend using `argparse` for this use case.
6. Commit the changes with a meaningful message.
7. Push the changes to the remote repository.
8. Do the same for the EDA notebook:<br>
    - Create script `plots.py` and functions for the EDA notebook, and refactor it.
9. Commit the changes with a meaningful message.
10. Push the changes to the remote repository.
11. Create a pull request to merge `feat/notebooks-to-scripts` into the main branch.
12. Merge the pull request on GitHub.
