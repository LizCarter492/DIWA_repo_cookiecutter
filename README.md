# The DIWA Standard Repository
This repository template is designed to help users meet standards for Findable, Accessible, Interoperable, and Reproducible research. A standard repository ensures everything is stored, managed, and shared in a consistent, controlled, and efficient way.

This repository template utilizes a [Cookiecutter](https://www.cookiecutter.io/) template to guide users in generating a standard research repository:

## Repository Structure

| Folder/File | Description |
|-------------|-------------|
| notebooks/ | SE1–SE4 notebooks |
| inputs/ | minimal input data required, note most data should be stored on OGC/FAIR compliant databases and accessed from stable URLs |
| processed_data/ | analysis-ready datasets |
| model_data/ | Saved model outputs, model configuration files, predictions|
| figures/ | Figures, tables, graphs, and data-derivatives (e.g. summary statistics) displayed in manuscript text |
| ../raw_data/ | data downloaded from stable URLs/PDIs |
| ../processed_data/ | analysis-ready datasets |
| run_reproducibility.py | Reproducibility wrapper |
| Dockerfile | Reproducible container |
| CITATION.cff | Citation metadata, sourced directly from Zenodo |

## Instructions to use this tool
To create a new research repository from this cookiecutter template, open a bash terminal with Python 3+ installed. First, clone this repository:
```
git clone https://github.com/LizCarter492/DIWA_repo_cookiecutter
```
Install cookiecutter and check that the installation worked correctly:
```
pip install --user cookiecutter
cookiecutter --v
```
Use the cookiecutter command to initialize the cookiecutter template as a repository:
```
cookiecutter DIWA_repo_cookiecutter
```
Follow the prompts to modify the repository. Once the repository has been created, move inside of it using the `cd` command. [Follow these instructions to create a git and GitHub repository](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)

## Instructions to modify this tool
Fork the https://github.com/LizCarter492/DIWA_repo_cookiecutter repository. To change any elements of the template, navigate to the {{ cookiecutter.project_slug }}. All template elements are editable in this space. Once you are satisfied with your edits, push them to your forked repository, and submit a pull request.



