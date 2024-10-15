
# Manage dependencies and virtual environments 🛠️

- [Section 1: Introduction](#introduction)
- [Section 2: Dependencies management](#dependencies-management)
  - [Managing dependencies with requirements.txt](#managing-dependencies-with-requirementstxt)
  - [Pip and PyPi](#pip-and-pypi)
  - [Managing dependencies with requirements.in](#managing-dependencies-with-requirementsin)
  - [Separate regular and dev dependencies](#separate-regular-and-dev-dependencies)
- [Section 3: Virtual environment](#virtual-environment)
  - [What is a virtual environment ?](#what-is-a-virtual-environment)
  - [How to create a virtual environment ?](#how-to-create-a-virtual-environment)
  - [How to use a virtual environment ?](#how-to-use-a-virtual-environment)
- [Section 4: Poetry](#poetry)
  - [Setting up Poetry](#setting-up-poetry)
  - [Poetry Basic usage](#poetry-basic-usage)
  - [Separation of dev and regular dependencies](#separation-of-dev-and-regular-dependencies)
- [Exercises](#exercises)
    - [✅ Module validation](#✅-module-validation)


## Introduction
In machine learning dependencies are crucial to run our code, but they can vary across different projects. One project might require a specific version of a library that could conflict with another project’s needs. By using a virtual environment, you create an isolated workspace and you ensure that each project has the exact versions of libraries it requires, avoiding conflicts and compatibility issues.


Virtual environments and managing dependencies are crucial to:
- **Reproducibility**: With a virtual environment, all dependencies are captured in a consistent state. This makes it easy to reproduce the same setup on different machines, ensuring that the project behaves the same way, whether it’s running on a developer’s local machine or in production.
- **Isolation**: Each project is self-contained, reducing the risk of breaking other projects when adding, updating, or removing dependencies.


Another concept we need to ensure reproducibility and isolation is **Docker**. **Docker** is a tool that allows developers to package applications, along with all their dependencies, into lightweight, portable containers. These containers include everything the application needs to run, such as the code, runtime, libraries, and environment settings. By doing this, **Docker** ensures that the application behaves the same way across different environments, regardless of the underlying system. We will see docker in details in another module.



## Dependencies management
### Managing dependencies with requirements.txt

In Python projects, the `requirements.txt` file is used to specify the external libraries and dependencies needed for the project to run correctly. Each line in the file typically contains the name of a package and an optional version specifier, ensuring that the right version of a library is installed.

Example of `requirements.txt`:

```
pandas==1.2.3
numpy==1.20.1
scikit-learn==0.24.1
lightgbm==3.2.1
```

To install dependencies with `pip` we need to run:

`pip install -r requirements.txt`

### Pip and PyPi

**What is pip ?** <br>
**pip** is the standard package manager for Python, which allows users to install and manage additional libraries and dependencies that are not included in the standard library.

**What is PyPi ?** <br>
pip connects to the **Python Package Index (PyPI)**, a repository of software for the Python programming language, to download and install packages. This makes it easy for developers to integrate and use these packages in their own projects.

Developers can upload their Python modules and packages to PyPI to make them available to others. When a user runs `pip install package-name`, pip will download the package from PyPI if it is available there.

**PyPi** is called **package registry** which is a centralized repository or service that hosts and manages software packages, libraries, or modules. It allows developers to share, distribute, and install these packages easily across different projects. It's the most well-known package registry In the context of Python.


### Managing dependencies with requirements.in
`requirements.txt` is typically used to list the packages and their specific versions that are necessary for the project to run. However, sometimes this file alone is not enough, especially when you need more control over your dependencies.

This is where `requirements.in` comes into play. `requirements.in` is often used as a “source” file for defining high-level dependencies in a more flexible and manageable way. It typically contains top-level dependency specifications (without locking versions), and is processed by tools like `pip-compile` from the `pip-tools` package to generate a requirements.txt file.

This approach is especially useful in complex projects where dependencies and their version compatibility can become difficult to maintain manually.

Example of `requirements.in`:
```
pandas
scikit-learn
```

Go from `requirements.in` to `requirements.txt`:
```bash
 pip-compile requirements.in
```

Example of the generated `requirements.txt`:
```
joblib==1.4.2
    # via scikit-learn
numpy==2.1.2
    # via
    #   pandas
    #   scikit-learn
    #   scipy
pandas==2.2.3
    # via -r requirements.in
python-dateutil==2.9.0.post0
    # via pandas
pytz==2024.2
    # via pandas
scikit-learn==1.5.2
    # via -r requirements.in
scipy==1.14.1
    # via scikit-learn
six==1.16.0
    # via python-dateutil
threadpoolctl==3.5.0
    # via scikit-learn
tzdata==2024.2
    # via pandas
```

### Separate regular and dev dependencies
A good practice to always keep in my mind to separate the dependencies into two categories, regular and dev ones. This separation is between regular dependencies which are required and used to run our code (ex: pandas, scikit-learn) and dev dependencies which are only needed during the development phase (ex. pre-commit, ruff, bandit, etc…).

By separating these:
- You maintain a clean production environment by only installing the packages that are necessary for running the application. And that it's not cluttered with unnecessary packages, which can reduce the risk of conflicts and minimize the deployment size and time.

- Moreover, separating these dependencies also makes it easier for other developers to understand which packages are essential for the application to run and which are just for development purposes.


To implement this separation, you can create a `requirements-dev.in` file alongside your `requirements.in` file (and thus a `requirements-dev.txt` file). The `requirements-dev.in` file will contain all the development dependencies.



## Virtual environment
### What is a virtual environment ?

A virtual environment is an isolated workspace where you can install dependencies and packages required for a specific project, without affecting the system-wide Python installation or other projects. This isolation ensures that different projects can have different versions of the same package without conflicts, which is particularly important when working on multiple projects with distinct requirements. Virtual environments help to avoid version mismatches and make project dependencies more manageable and reproducible.

### How to create a virtual environment ?
In this guideline we will cover two approaches to handle virtual environments venv and conda.

**Using venv (Python’s built-in tool):**

```bash
python -m venv myenv
```

This will create a virtual environment called myenv.

**Using conda:**

1- 	Install Conda (if not installed already, e.g., via [Anaconda](https://www.anaconda.com/) or [Miniconda](https://docs.anaconda.com/miniconda/)).<br>
2- Create a virtual environment:
```bash
conda create --name myenv
```

This will create a new environment called myenv with the default Python version.

### How to use a virtual environment ?
To install dependencies inside a virtual environment, we need to activate it first and then run the installation command to install dependencies inside of it.

**Using venv (Python’s built-in tool):**

1) Activate the virtual environment:

On Windows:
```bash
myenv\Scripts\activate
```

On macOS/Linux:
```bash
source myenv/bin/activate
```


2) Install dependencies (e.g., numpy package):
```bash
pip install numpy
```

3) Deactivate the environment:
```bash
deactivate
```

**Using conda:**
1) Activate the virtual environment:
```bash
conda activate myenv
```

2) Install dependencies (e.g., numpy package):
```bash
conda install numpy
```

3) Deactivate the environment:
```bash
conda deactivate
```



## Poetry

Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you. Poetry offers a lockfile to ensure repeatable installs, and can build your project for distribution.

Unlike other tools like pip and virtualenv, Poetry is a single tool that offers dependency management, packaging, and virtual environment creation.

### Setting up Poetry

To install poetry run the following command:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

You may need to add Poetry to your PATH if yout system don't detect it automatically. You can find more details about installation [here](https://python-poetry.org/docs/#installation)

To check that poetry was successfully installed run
```bash
poetry --version
```
If you see something like `Poetry (version 1.8.0)`, your install is ready to use!

### Poetry Basic usage

To start with poetry you need to create a new project if you don't already have one
```bash
poetry new my_project
```

Or use poetry for an existing project with:
```bash
poetry init
```
This will create the `pyproject.toml` (or modify it if it exists) and add:
- A section that contains metadata about your project. `[tool.poetry]`
- A section that defines the project's dependencies `[tool.poetry.dependencies]`
- A section that defines how the package should be built `[build-system]`


Once your project is initialized, you can add dependencies using the poetry add command.<br>
For example, to add the requests library, you can run:
```bash
poetry add requests
```
This command will update the `pyproject.toml` file and the `poetry.lock` file.


The `poetry.lock` file locks the versions of your dependencies, ensuring that every user of your project gets the same versions of the dependencies.

The `poetry.lock` file is crucial for maintaining consistency across different environments. It ensures that the exact versions of the dependencies are used every time the project is built, preventing unexpected changes or conflicts.


If we want to remove a dependency we can run the `poetry remove` command:

```bash
poetry remove requests
```

**Update dependencies:**
```bash
poetry update
```

**Run a command within the virtual environment:**
```bash
poetry run python script.py
```

More info about poetry basic usage can be found [here](https://python-poetry.org/docs/basic-usage/)

### Separation of dev and regular dependencies
Separation of dev and regular dependencies is also crucial with poetry<br>
To achieve this we need to add regular dependencies as follow:
```bash
poetry add requests
```

and development dependencies with the `--dev` flag as follow
```bash
poetry add --dev pytest
```

After adding dependencies, your `pyproject.toml` will look something like this:

```toml
[tool.poetry]
name = "your_project"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = "^3.8"
requests = "^2.25.1"

[tool.poetry.dev-dependencies]
pytest = "^6.2.4"
```

## Exercises

### ✅ Module validation
In this exercise we will manage dependencies with poetry
1. Create a new branch named `feat/poetry`.
2. Install poetry to be able to use it
3. Set up poetry and check that the pyproject.toml have been correctly updated
4. Add the required regular and dev dependencies
5. Check that your code work with the new environment (run the notebook)
6. Modify the CI to run commands with poetry
7. Create a pull request to merge `feat/poetry` into the main branch.
8. Merge the pull request on GitHub.

Thanks for completing this module on managing dependencies and virtual environments! 🎉 In the [next module](./08_wrap_up), we will wrap up everything we've learned in this first part of the hands-on. See you there!
