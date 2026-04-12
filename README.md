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

## TO DO:
1. Instructions to initialize Zenodo account
2. The run_reproducibility.py should ensure end-to-end reproducibility of SE1-4, create dockerfile, and configure repo for binderhub.
3. SE1 should train on DIWA DDAS protocols and include instuctions on use of DIWA Data Lake
4. SE2 should include more examples of standard geospatial processing operations and introduce the concept of exploratory data analysis
5. SE3 should introduce the DIWA model interoperability framework
6. SE4 should include examples of interactive data visualizations (e.g. ipyleaflet, voila, dash)
7. We should add a tool to automate authentication protocols for common APIs (if needed)
8. Set up github actions for Docker + BinderHub 
Contact elizabeth.carter@oulu.fi with any questions/comments/concerns.



