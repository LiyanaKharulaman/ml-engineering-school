<div align="center">

# AXA MLEng School

</div>

## Overview
This repository contains the code and resources for the hands-on sessions of the AXA MLEng School. The goal of this school is to provide practical experience into MLOps practices, after completing the necessary courses on YesLearning.
TODO: Add more details about the project
TODO: Add links to YesLearning courses

To start the hands-on exercises, please follow the instructions found in the [guidelines folder](./guidelines) folder at the root of the repo. Follow the instructions in order.

### [Part 1 - Fundamentals of DevOps](./guidelines/Part-1)

- [**1.0 - Setup & Prerequisites**](./guidelines/Part-1/00_setup.md)
- [**1.1 - Git 101**](./guidelines/Part-1/01_git_101.md)
- [**1.2 - Notebooks to Scripts**](./guidelines/Part-1/02_notebooks_to_scripts.md)
- [**1.3 - Linting & Formatting**](./guidelines/Part-1/03_linting_formatting.md)
- [**1.4 - Continuous Integration**](./guidelines/Part-1/04_continuous_integration.md)
- [**1.5 - Unit Testing**](./guidelines/Part-1/05_unit_testing.md)
- [**1.6 - Code Documentation**](./guidelines/Part-1/06_code_documentation.md)
- [**1.7 - Dependency Management**](./guidelines/Part-1/07_dependency_management.md)
- [**1.8 - Wrap Up**](./guidelines/Part-1/08_wrap_up.md)

### [Part 2 - Package your model as a product](./guidelines/Part-2)

WIP

## Getting Started
To get started with this project, follow the instructions below.

### Prerequisites
- Python 3.10 or higher
- pip (Python package installer)

### Installation
Clone the repository:
    ```
    git clone git@github.com:artefactory-fr/axa-mleng-school-original.git
    ```

Refer to the instructions in the module on how to set up the ssh connection and where to clone the repo in Azure.



## Repository structure
The repo structure is as follow:
```
.
├── .github
│   └── workflows               <-- GitHub Actions workflows for CI/CD
├── guidelines                  <-- Guidelines to complete the hands-on tasks
├── lib                         <-- Library python code used in the project
├── notebooks                   <-- Jupyter notebooks
├── .gitignore                  <-- Specifies files and directories to be ignored by git
├── .pre-commit-config.yaml     <-- Configuration for pre-commit hooks
├── Makefile                    <-- Makefile for automating tasks
├── pyproject.toml              <-- Project configuration file for the project
├── README.md                   <-- Overview of the readme
├── requirements-dev.txt        <-- Development dependencies
├── requirements.in             <-- Input file for pip-compile to generate requirements.txt
└── requirements.txt            <-- Project dependencies
```

## Contact
For any questions or concerns, please open an issue or contact [christophe.reigner@axa.com].
