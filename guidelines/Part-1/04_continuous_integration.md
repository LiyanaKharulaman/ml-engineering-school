# Continuous Integration: Automating Your Workflow 🚀

Welcome to the third module of the MLOps course! In this module, we will introduce you to the concepts of continuous integration (CI), which are essential for automating your development workflow. By the end of this module, you will be familiar with the following topics:

- [Section 1: What is Continuous Integration](#section-1-what-is-continuous-integration)
- [Section 2: Why Continuous Integration is Important](#section-2-why-continuous-integration-is-important)
- [Section 3: What Continuous Integration Includes](#section-3-what-continuous-integration-includes)
- [Section 4: Setting up Continuous Integration with GitHub Actions](#section-4-setting-up-continuous-integration-with-github-actions)
- [Exercise](#exercise)

## Section 1: What is Continuous Integration

Continuous Integration (CI) is a development practice where developers integrate code into a shared repository frequently, preferably several times a day. Each integration is verified by an automated build and automated tests to detect integration errors as quickly as possible. This practice leads to significantly reduced integration problems and allows teams to develop cohesive software more rapidly.

## Section 2: Why Continuous Integration is Important

- **Early Detection of Issues**: CI helps in identifying issues early in the development process, making it easier to fix bugs and errors.
- **Improved Code Quality**: Automated tests and builds ensure that the codebase remains in a good state, leading to higher code quality.
- **Faster Development**: By automating repetitive tasks, CI allows developers to focus on writing code, leading to faster development cycles.
- **Enhanced Collaboration**: CI facilitates better collaboration among team members by ensuring that the codebase is always in a deployable state.

## Section 3: What Continuous Integration Includes

- **Code Quality Checks**: Running linting and formatting tools to ensure that the code adheres to predefined standards.
- **Automated Tests**: Running automated tests to verify that the code works as expected.
- **Automated Builds**: Automatically compiling and building the code to ensure that it is in a deployable state.

## Section 4: Setting up Continuous Integration with GitHub Actions

GitHub Actions is a powerful CI/CD tool that allows you to automate your workflow directly from your GitHub repository. You can learn more about GitHub Actions [here](https://docs.github.com/en/actions). Below are the steps to set up a CI pipeline using GitHub Actions.

### Step 1: Create a GitHub Actions Workflow File

Create a `.github/workflows/ci.yml` file in your repository with the following content:

```yaml
name: CI

on:
  push:
    branches:
      - '*'
  pull_request:
    branches:
      - '*'

jobs:
  ci:
    name: Launching CI
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.9', '3.10', '3.11']

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.8'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install ruff

    - name: Run pre-commit hooks
      run: ruff check lib
```

### Step 3: Commit and Push

Commit and push the changes to your repository. GitHub Actions will automatically run the CI pipeline on every push to the specified branches.

## Exercise

Now that you have learned about continuous integration, it's time to put your knowledge into practice. Complete the following exercise to reinforce your understanding:

1. Create a `.github/workflows/ci.yml` file in your repository with the content provided in Step 1.
2. Ensure you have a `.pre-commit-config.yaml` file in your repository with the content provided in Step 2.
3. Add the following steps using github actions:
    - Checkout
    - Set up Python
3. Add the following steps using bash commands:
    - Install dependencies to run pre-commits (pre-commit, ruff, ...)
    - Run pre-commit on all files in CI
4. Commit and Push your changes.
5. Verify that the CI pipeline runs successfully on GitHub Actions.
6. Create a PR and merge your changes.


By completing this exercise, you will have set up a CI pipeline using GitHub Actions to run pre-commit hooks on every push to the specified branches.

🚀 Happy coding! 💻

Thanks for completing this module on continuous integration! 🎉 In the [next module](./05_unit_testing), we will dive into setting up unit tests to ensure the correctness of your code. See you there!
