# Usage: with`poetry` + `pyenv`

## Set local `pyenv` environment

Let's say you want to create an environment using python version 3.10.6 (default: 3.10.6)

```bash
pyenv install 3.10.6
```
Then navigate to the root directory and make it your local version:

```bash
pyenv local 3.10.6
```

This creates a `.python-version` file. During cookie creation this should have prompted you for this for convenience

## Install dependencies and create the virtual env in `poetry`

```bash
# Install required libraries
poetry install
```

This will install the dependencies and the pymc_statespace package and create a virtual environment and virtual shell. You can exit the virtual shell with crtl+d or `exit` in terminal.

## Resuming work

Next time you enter into the directory, `pyenv` will detect and activate local python version and then you can restart the shell:

```bash
poetry shell
```