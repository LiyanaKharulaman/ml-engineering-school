# Code Documentation 📚

Welcome to the Code Documentation module! In this section, we'll delve into the significance of clear and concise documentation for your code, not only to make it more understandable and user-friendly but also to facilitate debugging. You'll learn how to write effective docstrings, create informative README files, utilize MKDocs for documentation, and implement logging with Loguru to aid in tracking down and fixing bugs. Here's what we will cover in this module:

- [Section 1: Document your code](#section-1-document-your-code)
   - [Docstring](#docstring)
   - [Logging](#logging)
- [Section 2: Document your project](#section-2-document-your-project)
   - [README](#readme)
   - [Documentation in `docs/`](#documentation-in-docs)
   - [Setting up MKDocs](#setting-up-mkdocs)
   - [MKDocs](#mkdocs)
   - [Contributing.md](#contributingmd)
- [Exercises](#exercises)
    - [✅ Module validation](#✅-module-validation)


## Section 1: Document your code
### Docstring
#### What is a Docstring
Docstrings provide a way to document the purpose, behavior, and usage of functions, methods, classes, and modules. Well-written docstrings make code easier to understand, maintain, and use by others (or by yourself in the future).

#### Docstring Examples
A docstring starts and finishes with three double quotes: “““

Here's an example of a simple docstring:
```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
```

A detailed docstring should contain:
- Purpose: Clearly describe what the function, class, or method does (brief description)
- Arguments: List the parameters, their types, and what they represent.
- Return Values: Describe what the function returns and its type.
- Examples [Optional]: Provide usage examples, especially for complex functions, to show how they should be used.


Here's an example of a more detailed docstring:
```python
def fillna_with_mean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Replaces NaN values in numerical columns of the DataFrame with the mean value of the respective columns.

    Args:
        df: A pandas DataFrame that may contain NaN values in numerical columns.

    Returns:
        A pandas DataFrame where NaN values in numerical columns have been replaced
        by the mean of their respective columns.

    Example:
        >>> df = pd.DataFrame({"A": [1, 2, None], "B": [3, None, 5]})
        >>> fillna_with_mean(df)
           A    B
        0  1.0  3.0
        1  2.0  4.0
        2  1.5  5.0
    """
    df = df.fillna(df.mean())
    return df
```

**Docstring different style:**

There are different style of docstring, the three most common ones are:
1. **Google**: The one you see in the example above. It tends to require more horizontal space and easier to read for short and simple docstrings.

2. **Numpy**: Tends to require more vertical space and is easier to eead for long and in-depth docstring

Here's an example:
```python
def fillna_with_mean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Replaces NaN values in numerical columns of the DataFrame with the mean value of the respective columns.

    Parameters
    ----------
    df : pd.DataFrame
        A pandas DataFrame that may contain NaN values in numerical columns.

    Returns
    -------
    pd.DataFrame
        A pandas DataFrame where NaN values in numerical columns have been replaced
        by the mean of their respective columns.

    Examples
    --------
    >>> df = pd.DataFrame({"A": [1, 2, None], "B": [3, None, 5]})
    >>> fillna_with_mean(df)
       A    B
    0  1.0  3.0
    1  2.0  4.0
    2  1.5  5.0

    """
    df = df.fillna(df.mean())
    return df
```


3. **reST**: the default docstring style used by Python’s Sphinx documentation generator. It uses directives and markup to structure the docstring, which is useful when auto-generating documentation.

Here's an example:
```python
def fillna_with_mean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Replaces NaN values in numerical columns of the DataFrame with the mean value of the respective columns.

    :param df: A pandas DataFrame that may contain NaN values in numerical columns.
    :type df: pd.DataFrame
    :return: A pandas DataFrame where NaN values in numerical columns have been replaced by the mean of their respective columns.
    :rtype: pd.DataFrame

    **Example**::

        >>> df = pd.DataFrame({"A": [1, 2, None], "B": [3, None, 5]})
        >>> fillna_with_mean(df)
           A    B
        0  1.0  3.0
        1  2.0  4.0
        2  1.5  5.0
    """
    df = df.fillna(df.mean())
    return df
```



#### Important notes:
- Be consistent with formatting across all your docstrings. This makes the code easier to navigate.
- Don’t describe the obvious: Avoid unnecessary jargon. Explain things as concisely and clearly as possible.
- Update your docstrings regularly whenever you update the code. Outdated docstrings can lead to confusion.



### Logging
#### Setting up Loguru
Loguru is a popular third-party logging library that simplifies logging in Python. It has concise syntax and powerful features, making it an excellent alternative to the standard logging module.

To install Loguru run the following command:
```bash
pip install loguru
```

#### Basic loguru usage

The most basic way to use Loguru is by importing the logger object from the loguru package.
```python
from loguru import logger

logger.info("This is an info message")
logger.error("This is an error message")
```

The output in the terminal should look like this:

```
2022-08-10 11:16:59.511 | INFO | __main__:<module>:3 - This is an info message
2022-08-10 11:16:59.537 | ERROR | __main__:<module>:4 - This is an error message
```

The output contains the following details:
- The timestamp
- The log level
- The file location, scope and line number.
- The log message


Here are important log levels in Loguru:
- `logger.debug`: Used by developers to record messages for debugging purposes.
- `logger.info`: Used to record informational messages that describe the normal operation of the program.
- `logger.warning`: Used to indicate an unusual event that may require further investigation.
- `logger.error`: Used to record error conditions that affected a specific operation.
- `logger.critical`: Used to record critical conditions that prevent a core function from working.

2. Implement docstrings for all functions within our library to provide clear documentation and usage instructions.
3. Create a comprehensive README file that outlines the project, installation instructions, and usage examples.
4. Set up MKDocs for the project to generate a user-friendly documentation website.
5. Integrate logging into our library functions, ensuring to include both informational and error logs where appropriate.




## Section 2: Document your project
### README
#### What is a README
A README is typically a plain text or Markdown file (README.md) that is placed in the root directory of a project repository. It acts as a first point of contact for anyone exploring or using the project.

In simple words, we can describe a README file as a guide that gives users a detailed description of the project.

A well-crafted README enhances first impressions, guides usage, improves collaboration, clarifies purpose, and reduces support requests.

#### What to Include in your README
1. Project's Title: A brief and descriptive title of the project.
2. Project Description: Allows to show off your work to other developers:
    - What your application does,
    - Why you used the technologies you used,
    - Some of the challenges you faced and features you hope to implement in the future
3. Table of Contents (Optional): Useful for longer README files.
4. Installation: Step-by-step instructions on prerequisites how to install and set up the project.
5. Usage: Examples of how to use the project.
6. Contributing: Guidelines for people who want to contribute to the project.
7. License: Specify the project’s license (e.g., MIT, Apache 2.0)


### Documentation in `docs/`
The docs/ directory typically serves as the central repository for all project-related documentation. This folder houses essential information for developers, contributors, and end-users, to understand and use the project effectively


Here’s an example what you can put in the `docs/` directory :

1. Usage Guide:
- Step-by-step instructions for running the machine learning models, including input formats, sample datasets, and expected output.
- Examples showcasing how to make predictions, train models, or test the pre-trained model on new data.
2. API Documentation:
- A detailed description of the project’s Python functions, classes, and modules, including parameters, return types, and example usage.
- Generated using tools like Sphinx, documenting the core components such as data loaders, preprocessing functions, model definitions, and evaluation metrics.
3. Data documentation:
- Documentation and examples of the data structure used in this project.
- Information on how to access and use the datasets, including any necessary scripts or commands.
- Details on the source and licensing of the data, ensuring users understand the permissions and restrictions.
4. Model Training Instructions:
- A dedicated section on how to train models from scratch, including hyperparameter tuning, data augmentation, and experiment tracking.
- Instructions on how to reproduce the experiments, often with notebooks or scripts provided as examples.




### MKDocs
MkDocs is a static site generator that’s particularly well-suited for creating project documentation. It’s designed to be simple to use and creates a searchable, well-organized site from Markdown files.

#### Setting up MKDocs
To install MkDocs run the following command:
```bash
pip install mkdocs
```

Once installed, you can verify the installation by running:
```bash
mkdocs --version
```

#### Basic MKDocs usage

To initializes a new MkDocs project in the root of your repository run the following command:
```bash
mkdocs new .
```
This will create:
- A `mkdocs.yml` configuration file
- A new directory called docs containing `index.md` which is the homepage of the documentation website in Markdown

To start a local development server, run the following command:
```bash
mkdocs serve
```
You can visit the site in your browser at http://127.0.0.1:8000/.

To add new new pages for your site, you just need to add the Markdown file of the page in the `docs` folder.

More info about MKDocs here: https://www.mkdocs.org/getting-started/

### Contributing.md
A CONTRIBUTING.md file is an essential part of any open-source project, serving as a guide for contributors on how to engage with the project. The primary goal of a CONTRIBUTING.md file is to ensure that potential contributors understand how to contribute effectively to the project. It sets clear expectations and provides necessary information to help them navigate the contribution process.

Key Sections to Include:
1. Introduction: A brief overview of the project and its goals, encouraging potential contributors to get involved.
2. Code of Conduct: A statement about the expected behavior of contributors, promoting a welcoming and respectful environment.
3. How to Contribute:
    - Reporting Issues: Guidelines for submitting bug reports or feature requests.
	- Submitting Code: Instructions for forking the repository, creating branches, and submitting pull requests (PRs). This section can also cover the preferred coding style, commit message conventions, and how to run tests.
4. Development Setup: Detailed steps on how to set up the development environment, including dependencies, configuration, and any tools or frameworks used in the project.
5. Testing: Information on how to run tests, including any specific test cases that should be prioritized or are essential for contributions.
6. Documentation: Guidelines for updating documentation as part of contributions, including how to build and preview documentation changes.
7. Acknowledgments: Recognition of contributors and a call for community involvement.


## Exercises

### ✅ Module validation
1. Create a new branch named `feat/code-documentation`.
2. Implement docstrings for all functions within our library to provide clear documentation and usage instructions.
3. Set up MKDocs for the project to generate a user-friendly documentation website
4. Write some documentation inside the `docs` folder with multiple pages and visualize it in your MKDocs website
5. Integrate logging into our library functions, ensuring to include both informational and error logs where appropriate.
6. Create a pull request to merge `feat/code-documentation` into the main branch.
7. Merge the pull request on GitHub.
