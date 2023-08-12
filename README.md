# Naruto Image Classifier

This is a template repository of using the Flask framework in Python to predict what character from the "Naruto" anime series that a trained machine learning model thinks it would be classified under with an image.

**Classifier Label**

The Naruto anime character.

Possible labels:

- Jiraiya
- Sakura
- Sasuke

## Instructions

The `app.py`, `index.html`, and `predict.html` files contain starter code with key features missing. Information on what code is missing is provided in comments.

**GitHub**

Login to GitHub and create an empty GitHub repository.

**Terminal**

Open a terminal window and navigate to your desired path.

1. Set Git credentials

Replace **github-username** and **github-email-address** with your GitHub's username and email address, respectively.

```
git config --global user.name "github-username"
git config --global user.email "github-email-address"
```

2. Clone the repository

```
git clone https://github.com/chticer/narutoimageclassifiertemplate
```

```
cd narutoimageclassifiertemplate
```

3. Update remote repository location

Replace **github-repository-url** with the GitHub repository URL that was created.

```
git remote set-url origin github-repository-url.git
```

4. Initialize Git Large File Storage

For this repository, trained models may be too big that would exceed GitHub's normal file size limit. This will cause issues when trying to push the files to your GitHub repository.

```
git lfs install
```

```
git lfs track "*.h5"
```

See the [Git Large File Storage website](https://git-lfs.com/) for more information.

**Visual Studio Code**

Open the cloned repository (File > Open Folder).

Add any Azure Machine Learning workspace models created with this dataset into the `models` folder. One model is included.

Run the Flask application (open `app.py` then Run > Run Without Debugging).

Stage, commit, and push files using Source Control on the left side.

**Azure App Service Deployment**

Create an Azure app service.

1. Go to https://portal.azure.com/ and search for the "App services" resource.
1. Click Create > Web App. Fill in the following fields then click Review + create:
    - **Subscription**: Select your Azure subscription.
    - **Resource Group**: Select an existing one or create a new one.
    - **Name**: Enter an unique website name.
    - **Runtime stack**: Select a Python version.
    - **Region**: Select the closest region.
    - **Linux Plan**: Create a new app service plan.
    - **Pricing plan**: Select a plan based on your needs.
1. Once the resource has been deployed, go to the resource.
1. On the left side, click Deployment > Deployment Center.
1. Click the Settings tab. Fill in the following fields then click Save:
    - **Source**: GitHub (authorize your GitHub account with Microsoft Azure App Services if necessary)
    - **Organization**: Select your GitHub username.
    - **Repository**: Select the GitHub repository.
    - **Branch**: Select the origin branch of the GitHub repository.
1. View the website. To find the website URL, on the left side, click Overview. The website URL will be shown next to Default domain.

## Special Thanks

This repository is part of an Azure Machine Learning workshop conducted with students, which was made possible by a grant from the Department of Homeland Security, at The University of Texas Rio Grande Valley on Saturday, August 12, 2023.

**Workshop Leaders**
- @alfazick (Dr. Askar Nurbekov)
- @chticer (Mr. Charlie Ticer)
- @etomai (Dr. Emmett Tomai)

We would also like to thank the students for their participation and the IT and department administrative staff and student workers for their help, time, and resources in this workshop.
