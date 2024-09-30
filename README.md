<div align="center">

# AXA MLEng School

</div>

## Overview
This repository contains the code and resources for the hands-on sessions of the AXA MLEng School. The goal of this school is to provide practical experience into MLOps practices, after completing the necessary courses on YesLearning.


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

### Guidelines
To start the hands-on exercises, please follow the instructions found in the [guidelines folder](./guidelines) folder at the root of the repo. Follow the instructions in order.


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
