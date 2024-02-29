---
page_type: sample
description: "A minimal sample app that can be used to demonstrate deploying FastAPI apps to Azure App Service."
languages:
- python
products:
- azure
- azure-app-service
---

# Project Structure

This project consists of the following directories and files:

```
.
├── .git/                        # Git source directory for repository management
├── .github/                     # GitHub-specific metadata and configuration
├── app/
│   └── backend/                 # Backend code for the FastAPI application
│       ├── main.py              # Main FastAPI application source file
│       └── requirements.txt     # Python dependencies for the FastAPI application
├── infra/                       # Infrastructure as code (IaC) configurations
├── static/                      # Static files for the web application
├── templates/                   # Template files for the web application
├── .gitignore                   # Specifies intentionally untracked files to ignore
├── CHANGELOG.md                 # Markdown file containing the changelog
├── CONTRIBUTING.md              # Guidelines for contributing to the project
├── LICENSE.md                   # The license agreement for the project
├── README.md                    # The README for the project with detailed information
└── startup.sh                   # Shell script to start up the project
```

Each directory and file has a specific purpose:

- `.git/`: Contains all of the Git data and configuration files.
- `.github/`: Houses GitHub workflows and project settings.
- `app/backend/`: Contains all backend-related code for the FastAPI application, including the main entry point (`main.py`) and dependencies (`requirements.txt`).
- `infra/`: Includes all Terraform or other IaC files for setting up infrastructure.
- `static/`: Holds static assets like images, CSS, and JavaScript files.
- `templates/`: Contains HTML templates that are used to render views/pages.
- `.gitignore`: Lists files and directories that should not be tracked by Git.
- `CHANGELOG.md`: Documents all the changes made over time for each version.
- `CONTRIBUTING.md`: Provides guidelines for how to contribute to the project.
- `LICENSE.md`: Describes the licensing of the project.
- `README.md`: Offers a detailed description of the project, how to install, configure, and use it.
- `startup.sh`: A shell script to start the project services or server.

# Deploy a Python (FastAPI) web app to Azure App Service - Sample Application

This is the sample FastAPI application for the Azure Quickstart [Deploy a Python (Django, Flask or FastAPI) web app to Azure App Service](https://docs.microsoft.com/en-us/azure/app-service/quickstart-python). For instructions on how to create the Azure resources and deploy the application to Azure, refer to the Quickstart article.

Sample applications are available for the other frameworks here:
- Django [https://github.com/Azure-Samples/msdocs-python-django-webapp-quickstart](https://github.com/Azure-Samples/msdocs-python-django-webapp-quickstart)
- Flask [https://github.com/Azure-Samples/msdocs-python-flask-webapp-quickstart](https://github.com/Azure-Samples/msdocs-python-flask-webapp-quickstart)

If you need an Azure account, you can [create one for free](https://azure.microsoft.com/en-us/free/).

## Local Testing

To try the application on your local machine:

### Install the requirements

`pip install -r requirements.txt`

### Start the application

`uvicorn main:app --reload`

### Example call

http://127.0.0.1:8000/

## Next Steps

To learn more about FastAPI, see [FastAPI](https://fastapi.tiangolo.com/).
