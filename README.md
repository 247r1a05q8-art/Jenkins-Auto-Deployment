# Automated Git-to-Production Deployment Using Jenkins

## Project Overview

This project demonstrates an automated CI/CD pipeline in which source code is stored in Git, Jenkins automatically builds and tests the application, creates a Docker image, and deploys the application as a production container.

## Pipeline

Git Push
→ Jenkins
→ Checkout
→ Install Dependencies
→ Run Tests
→ Build Docker Image
→ Deploy Container
→ Health Check

## Technologies

- Git / GitHub
- Jenkins
- Python
- Flask
- Pytest
- Docker
- Docker Compose

## Project Structure

Jenkins-Auto-Deployment/
- app/app.py
- app/requirements.txt
- app/templates/index.html
- tests/test_app.py
- Dockerfile
- docker-compose.yml
- Jenkinsfile
- .gitignore
- README.md

## Run Locally Without Jenkins

Install Python 3.10+ and Docker Desktop.

From the project directory:

    python -m pip install -r app/requirements.txt
    python -m pip install pytest
    python -m pytest tests -v

Build and run Docker:

    docker build -t jenkins-auto-deployment .
    docker run -d --name jenkins-auto-deployment -p 5000:5000 jenkins-auto-deployment

Open:

    http://localhost:5000

Health check:

    http://localhost:5000/health

## Jenkins Setup

1. Install Jenkins on your machine or a server.
2. Make sure Python, Git, and Docker are available to the Jenkins service.
3. Create a Jenkins Pipeline job.
4. Connect the job to your GitHub repository.
5. Select "Pipeline script from SCM".
6. Select Git as SCM.
7. Enter your repository URL.
8. Set the script path to:

    Jenkinsfile

9. Save the job.
10. Run "Build Now".

For automatic GitHub-triggered builds, configure a GitHub webhook to your Jenkins server and enable the appropriate GitHub webhook trigger in Jenkins.

## Important Windows Note

The supplied Jenkinsfile uses Windows batch commands (`bat`) because it is designed to run on a Windows Jenkins agent.

If Jenkins is running on Linux, replace the Windows `bat` commands with Linux `sh` commands.

## Expected Result

After a successful Jenkins build, the Docker container should be available at:

    http://localhost:5000

The home page displays the deployment status, environment, and Jenkins build number used as the application version.

## Academic Demonstration

For a project presentation, demonstrate:

1. Change a message in index.html.
2. Commit and push the change to GitHub.
3. Start the Jenkins pipeline.
4. Show Checkout.
5. Show automated tests.
6. Show Docker image creation.
7. Show container deployment.
8. Open the production application.
9. Explain the health-check endpoint.

## Security Note

For a real production system, use Jenkins credentials for repository and deployment secrets rather than placing passwords or tokens in the Jenkinsfile.
