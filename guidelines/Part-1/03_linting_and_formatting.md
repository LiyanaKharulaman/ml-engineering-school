# Linting and Formatting: Ensuring Code Quality and Consistency 🛠️

Welcome to the second module of the MLOps course! In this module, we will introduce you to the concepts of linting and formatting, which are essential for maintaining high-quality and consistent code. By the end of this module, you will be familiar with the following topics:

- [Section 1: Linting Code](#section-1-linting-code)
  - [What is Code Linting](#what-is-code-linting)
  - [Why Linting is Important](#why-linting-is-important)
  - [How to implement linting (flake8, pylint, ruff)](#how-to-implement-linting-flake8-pylint-ruff)
- [Section 2: Code Formatting](#section-2-code-formatting)
  - [What is Code Formatting](#what-is-code-formatting)
  - [Why Formatting is Important](#why-formatting-is-important)
  - [Tools such as Black and isort](#tools-such-as-black-and-isort)
- [Section 3: Security Code Scanning](#section-3-security-code-scanning)
  - [What is Security Code Scanning?](#what-is-security-code-scanning)
  - [Why Security Code Scanning is Important](#why-security-code-scanning-is-important)
  - [Tools such as Bandit](#tools-such-as-bandit)
- [Section 4: Ruff: The All-in-One Tool](#section-4-ruff-the-all-in-one-tool)
  - [Why you should use ruff](#why-you-should-use-ruff)
  - [How to use ruff](#how-to-use-ruff)
  - [Setting up Ruff](#setting-up-ruff)
- [Section 5: Pre-commits](#section-5-pre-commits)
  - [What are Pre-commits?](#what-are-pre-commits)
  - [Why Pre-commits are Important](#why-pre-commits-are-important)
  - [Setting up Pre-commits](#setting-up-pre-commits)
- [Exercise](#exercise)

## Section 1: Linting Code

### What is Code Linting?

Linting is the process of analyzing code to identify potential errors, bugs, stylistic errors, and suspicious constructs. It helps ensure that your code adheres to a set of predefined coding standards and best practices. Generic linting tools can be used across various programming languages to enforce these standards, ensuring code quality and consistency.

Whether generic or Python-specific, code linting is the automated checking of your source code for programmatic and stylistic errors. It helps in maintaining a consistent code style and catching potential bugs early in the development process, ultimately leading to higher quality and more maintainable code.

In the context of Python, linting is particularly important due to the language's emphasis on readability and simplicity. Python-specific linting tools, such as those adhering to the [PEP8 style guide](https://peps.python.org/pep-0008/), help maintain these principles by checking for compliance with Python's coding conventions. PEP8, the Python Enhancement Proposal 8, provides guidelines for writing clean and readable Python code, and tools like Flake8 and Pylint enforce these guidelines.


### Why Linting is Important

- **Early Error Detection**: Linting identifies errors and bugs at an early stage in the development process, significantly reducing the chances of encountering runtime errors. This proactive approach saves time and resources by catching issues before they escalate.
- **Enforcing Code Consistency**: By adhering to predefined coding standards, linting ensures that the codebase remains consistent and uniform. This consistency makes the code easier to read, understand, and maintain.
- **Enhancing Code Quality**: Linting promotes best practices and coding standards, leading to higher quality code. It helps in identifying potential issues related to code complexity, maintainability, and performance.
- **Facilitating Collaboration**: A consistent and well-linted codebase is easier for teams to work on collaboratively. It reduces misunderstandings and discrepancies, making it simpler for multiple developers to contribute to the same project seamlessly.
- **Improving Readability**: Linting enforces a clean and readable code style, which is crucial for both current and future developers who may work on the code. Readable code is easier to debug, extend, and refactor.
- **Automating Code Reviews**: Linting tools can automate parts of the code review process by flagging common issues and enforcing coding standards. This allows human reviewers to focus on more complex and nuanced aspects of the code.

### How to implement linting (flake8, pylint, ruff)

Linting can be implemented using various tools, each with its own strengths and focus areas. Below are introductions to three popular linting tools: Flake8, Pylint, and Ruff.

- **[Flake8](https://flake8.pycqa.org/en/latest/)**: Flake8 is a widely-used linting tool that checks for compliance with the PEP 8 style guide, as well as other common errors. It is lightweight and easy to integrate into your development workflow, making it a popular choice for many Python projects.

- **[Pylint](https://pylint.pycqa.org/en/latest/)**: Pylint is a comprehensive linting tool that goes beyond basic style checks to include code complexity analysis and potential bug detection. It provides detailed reports and suggestions for improving code quality, making it a valuable tool for maintaining robust and maintainable codebases.

- **[RECOMMENDED][Ruff](https://github.com/charliermarsh/ruff)**: Ruff is an all-in-one tool that combines linting, formatting, and security scanning. It aims to streamline the development process by offering a single tool that addresses multiple aspects of code quality. Ruff is particularly useful for teams looking to enforce consistent coding standards and improve overall code health, and is astonishingly fast.


#### Flake8

Flake8 is a popular linting tool that checks for PEP 8 compliance, as well as other common errors. It was the most widely used linter in the Python community, and it is still widely used today. Flake8 is a combination of several tools, including PyFlakes, pycodestyle, and McCabe, which work together to provide linting and style checking capabilities.

  ```bash
  # Install Flake8
  pip install flake8

  # Run Flake8 on a file or directory
  flake8 <file-or-directory>
  ```

You can configure Flake8 to ignore specific errors or customize its behavior using a configuration file. For more details, refer to the [Flake8 documentation](https://flake8.pycqa.org/en/latest/).


#### Pylint

Pylint is a comprehensive linting tool that goes beyond basic style checks to include code complexity analysis and potential bug detection. It provides detailed reports and suggestions for improving code quality, making it a valuable tool for maintaining robust and maintainable codebases.

  ```bash
  # Install Pylint
  pip install pylint

  # Run Pylint on a file or directory
  pylint <file-or-directory>
  ```

You can configure Pylint to ignore specific errors or customize its behavior using a configuration file. For more details, refer to the [Pylint documentation](https://pylint.pycqa.org/en/latest/).


#### [RECOMMENDED][Ruff](https://github.com/charliermarsh/ruff)**:

Ruff can be used as a linting tool in addition to its formatting and security scanning capabilities using the `check` command.
  ```bash
  # Run Ruff in linting mode on a file or directory
  ruff check <file-or-directory>
  ```

For more details, refer to the [Ruff Section](#section-4-ruff-the-all-in-one-tool).


## Section 2: Code Formatting


### What is Code Formatting

Formatting refers to the process of automatically arranging code according to a set of stylistic rules. This practice includes organizing and structuring code in a consistent manner, such as managing indentation, spacing, and line breaks. Consistent formatting ensures that the code is easier to read, maintain, and understand.

### Why Formatting is Important

- **Readability**: Consistently formatted code is easier to read and understand.
- **Reduced Diff Noise**: Proper formatting reduces unnecessary changes in version control diffs, making code reviews more efficient.
- **Focus on Logic**: Developers can focus on writing logic rather than worrying about code style.

### Tools such as Black, isort, and Ruff


#### Black

Black is an opinionated code formatter for Python. It formats code to follow a consistent style, reducing the need for manual formatting.
  ```bash
  # Install Black
  pip install black

  # Run Black on a file or directory
  black <file-or-directory>
  ```

You can configure Black using a `pyproject.toml` file. Here is an example configuration:
  ```toml
  [tool.black]
  line-length = 88
  target-version = ['py36', 'py37', 'py38', 'py39']
  skip-string-normalization = true
  ```

#### Isort

isort is a tool to sort and format import statements in Python files.
  ```bash
  # Install isort
  pip install isort

  # Run isort on a file or directory
  isort <file-or-directory>
  ```

You can configure isort using a `pyproject.toml` file or an `.isort.cfg` file. Here is an example configuration for `pyproject.toml`:
  ```toml
  [tool.isort]
  profile = "black"
  line_length = 88
  known_third_party = ["django", "flask"]
  ```

#### Ruff

Ruff can be used as a formatting tool in addition to its linting and security scanning capabilities using the `--format` flag.
  ```bash
  # Run Ruff in format mode on a file or directory
  ruff --format <file-or-directory>
  ```

For more details, refer to the [Ruff Section](#section-4-ruff-the-all-in-one-tool).

## Section 3: Security Code Scanning

### What is Security Code Scanning?

Security code scanning is the automated process of analyzing source code to identify and mitigate potential security vulnerabilities. This proactive approach ensures that the code is secure, free from common security issues, and maintains the integrity of the codebase. By integrating security code scanning into the development workflow, developers can detect and address vulnerabilities early, reducing the risk of security breaches and enhancing overall code quality.

### Why Security Code Scanning is Important

- **Prevent Security Breaches**: Identifying and fixing security vulnerabilities early can prevent potential security breaches.
- **Compliance**: Ensures that the code complies with security standards and regulations.
- **Trust**: Secure code builds trust with users and stakeholders.

### Tools for Security Code Scanning

Usually, only Bandit is enforced, while the use of other tools like Safety, SonarQube, and Snyk is optional.

#### Bandit
Bandit is a tool designed to find common security issues in Python code.
  ```bash
  # Install Bandit
  pip install bandit

  # Run Bandit on a directory
  bandit -r <directory>
  ```

#### Safety
Safety checks your installed dependencies for known security vulnerabilities.
  ```bash
  # Install Safety
  pip install safety

  # Check installed packages for vulnerabilities
  safety check
  ```

#### SonarQube
SonarQube is a platform for continuous inspection of code quality to perform automatic reviews with static analysis of code to detect bugs and vulnerabilities.
  ```bash
  # Run SonarQube scanner on a project
  sonar-scanner
  ```

#### Snyk
Snyk helps you find, fix, and monitor known vulnerabilities in your dependencies.
  ```bash
  # Install Snyk
  npm install -g snyk

  # Test your project for vulnerabilities
  snyk test
  ```

## Section 4: Ruff: The All-in-One Tool

Ruff is an extremely fast Python linter and code formatter that combines the functionality of multiple tools into one. It aims to be a drop-in replacement for tools like Flake8, Black, isort, and Bandit.

### What is Ruff?

Ruff is a comprehensive tool designed to streamline the development workflow by integrating multiple functionalities into a single, efficient tool. Unlike Flake8, which primarily focuses on linting, Ruff also includes formatting capabilities similar to Black, import sorting like isort, and security scanning akin to Bandit. This makes Ruff a versatile choice for Python developers who want an all-in-one solution that is not only faster but also reduces the complexity of managing multiple tools. Ruff's performance is orders of magnitude better, offering significant speed improvements and a unified toolchain that simplifies the development process.

### Why you should use Ruff

- **Performance**: Ruff is designed to be orders of magnitude faster than alternative tools. It's coded in Rust.
- **Unified Toolchain**: Combines linting, formatting, and security scanning into a single tool.
- **Ease of Use**: Simplifies the development workflow by reducing the need for multiple tools.
- **Comprehensive**: Implements over 800 built-in rules, covering a wide range of linting, formatting, and security checks.

### How to use Ruff

To use Ruff, you can install it via pip and run it on your codebase. Ruff commands are:

#### Linting with Ruff
  ```bash
  ruff check <file-or-directory>
  ```

#### Formatting with Ruff
  ```bash
  ruff format <file-or-directory>
  ```

#### Configuring Ruff rules

Ruff allows you to configure its rules to tailor the linting, formatting, and security checks to your project's needs. Below are examples of how to configure Ruff for specific tasks:

##### Formatting like isort
To format your imports like isort, you can use the following command:
  ```bash
  ruff check --fix --select I <file-or-directory>
  ```

##### Adding security checks with Bandit
To include security checks similar to Bandit, you can use the following command:
  ```bash
  ruff check --select S <file-or-directory>
  ```

You can also combine multiple configurations in a single command to leverage Ruff's comprehensive capabilities:
  ```bash
  ruff check --fix --select I,S <file-or-directory>
  ```

For more advanced configurations, you can create a `pyproject.toml` file in your project root and specify the rules and settings there. Here is an example configuration:
  ```toml
[tool.ruff]
target-version = "py38"
line-length = 99
exclude = [
    "tests/*",
]

[tool.ruff.lint]
ignore = [
    "D100",
    "D205",
    "D415",
]
select = [
    "B",    # bugbear
    "C4",   # comprehensions
    "C90",  # mccabe
    "D",    # docstrings
    "E",    # flake8
    "F",    # flake8
    "W",    # flake8
    "S",    # bandit
    "N",    # pep8-naming
    "RUF",  # ruff
    "I",    # isort
    "PD",   # pandas
]

[tool.ruff.lint.pydocstyle]
convention = "google"
  ```

### Setting up Ruff

In this exercise, you will configure Ruff to handle both linting and formatting for your project using a `pyproject.toml` file. Follow the steps below:

1. Create a `pyproject.toml` file in the root of your project.
2. Add the following configuration to the `pyproject.toml` file:
    - Line length should be set at 99.
    - rules should include "I", "S", "E", "F", "W"
    - docstrings format should be Google.
3. Run Ruff to check your codebase:
   ```bash
   ruff check <file-or-directory>
   ```
4. Run Ruff to format your codebase:
   ```bash
   ruff format <file-or-directory>
   ```

By completing this exercise, you will have configured Ruff to enforce linting and formatting rules with a line length of 99 and selected rules for import sorting, security checks, and flake8 compliance.

## Section 5: Pre-commits

### What are Pre-commits?

Pre-commits are hooks that run before a commit is made in a version control system. They are used to catch potential issues early in the development process. These scripts run automatically before a commit is finalized and can enforce code quality checks, run tests, and ensure that the codebase remains in a good state.

Pre-commits are of 3 types:
- on the shelf: Pre-commit hooks that are readily available and can be used out-of-the-box. For example, the `trailing-whitespace` hook from the `pre-commit-hooks` repository.
- extensions: Pre-commit hooks that extend the functionality of existing tools. For example, a pre-commit hook that runs `pytest` to ensure all tests pass before committing.
- local: Custom pre-commit hooks that are specific to your project. For example, a local pre-commit hook that runs `ruff check` to enforce linting rules tailored to your project's configuration.

Using pre-made pre-commits can be convenient, but it is often advised to use local pre-commits. Local pre-commits take into account the specific configuration and versions of tools like Ruff, Black, or isort that are used in your project. This ensures consistency and reliability, as the local setup is tailored to your project's unique requirements and environment.

### Why Pre-commits are Important

- **Early Detection**: Catch issues before they are committed to the codebase.
- **Consistency**: Ensure that all code meets the required standards before being added to the repository.
- **Automation**: Automate repetitive tasks, reducing the manual effort required for code reviews.

### Setting up Pre-commits

To set up pre-commits, you can use the `pre-commit` framework, which allows you to define a set of hooks that run automatically before each commit. These hooks can enforce code quality checks, run tests, and ensure that the codebase remains in a good state. The configuration for these hooks is specified in a `.pre-commit-config.yaml` file located at the root of your project.

Here is an example configuration for the `.pre-commit-config.yaml` file:
  ```yaml
  # .pre-commit-config.yaml
  repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
  ```

In this configuration:
- `repo` specifies the repository containing the pre-commit hooks.
- `rev` specifies the version of the repository to use.
- `hooks` lists the specific hooks to run, identified by their `id`.

By defining this configuration file, you can ensure that the specified hooks are executed every time a commit is made, helping to maintain code quality and consistency across your project.

### Exercise

Now that you have learned about linting, formatting, security code scanning, and pre-commits, it's time to put your knowledge into practice. Complete the following exercise to reinforce your understanding:

1. Create `.pre-commit-config.yaml`
    ```bash
    touch .pre-commit-config.yaml
    ```
2. Set up pre-commits to automate the following checks before committing your code:
   - Remove trailing whitespaces.
   - Check JSON, TOML, and YAML files for syntax errors.
   - Remove large files from commits.
   - Fix end-of-file issues.
   - Run `ruff format` to format your code.
   - Run `ruff check --fix` to apply linting fixes.
   - Run `ruff check` to enforce linting rules using the configuration specified in `pyproject.toml`.
3. Install pre-commits to run before committing
    ```bash
    pre-commit install
    ```
3. Run pre-commits on the whole repo
    ```bash
    pre-commit run --all
    ```

By defining this configuration file, you can ensure that the specified hooks are executed every time a commit is made, helping to maintain code quality and consistency across your project.

🚀 Happy coding! 💻

Thanks for completing this module on linting and formatting! 🎉 In the [next module](./04_continuous_integration), we will dive into setting up continuous integration (CI) pipelines to automate the testing and deployment of your code. See you there!
