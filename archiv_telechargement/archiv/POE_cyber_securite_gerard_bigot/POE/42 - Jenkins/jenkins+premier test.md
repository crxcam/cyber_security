To create a Jenkins pipeline that builds a Docker container to run a simple Python script that prints "Hello, World", you'll need a few components:
1. A Python script.
2. A Dockerfile to build the Docker image.
3. A Jenkinsfile to define the Jenkins pipeline.

### Step 1: Create the Python Script
First, create a Python script that prints "Hello, World". Let's call this script `hello.py`.

```python
# hello.py
print("Hello, World")
```

### Step 2: Create the Dockerfile
Next, create a Dockerfile that specifies how to build the Docker image. This Dockerfile will set up a Python environment, copy the script into the image, and configure the container to run the script.

```dockerfile
# Dockerfile
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY hello.py /app

# Command to run on container start
CMD ["python", "hello.py"]
```

### Step 3: Create the Jenkinsfile
Now, create a Jenkinsfile that defines the pipeline. This pipeline will build the Docker image and run the container.

```groovy
// Jenkinsfile
pipeline {
    agent any

    environment {
        // Define the Docker image name
        DOCKER_IMAGE = 'hello-world-python'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    docker.build(env.DOCKER_IMAGE)
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    // Run the Docker container
                    docker.image(env.DOCKER_IMAGE).run()
                }
            }
        }
    }
}
```

### Step 4: Set Up Jenkins and Docker
For Jenkins to be able to build Docker images and run Docker containers, you must ensure Jenkins has the appropriate permissions and Docker is installed on the Jenkins agent (or master if running without agents).

1. **Install Docker on the Jenkins Host**: Make sure Docker is installed where Jenkins jobs will run.
2. **Give Jenkins User Docker Permissions**: Add the Jenkins user to the Docker group so it can run Docker commands without `sudo`.
   ```bash
   sudo usermod -aG docker jenkins
   ```
3. **Restart Jenkins** after modifying user permissions to ensure the changes take effect.
4. **Install Docker Pipeline Plugin**: This Jenkins plugin offers various Docker-related pipeline steps. Install this plugin via Jenkins' "Manage Plugins" menu.

### Step 5: Run the Jenkins Job
Create a new job in Jenkins that uses this Jenkinsfile, and run the job. Jenkins will execute the pipeline, which builds the Docker image from the Dockerfile and runs the container to display "Hello, World".

### Additional Tips
- Ensure that Docker and Jenkins configurations are properly set to handle the build and execution environments.
- Manage Docker images and containers to avoid accumulating unused images and containers after multiple builds.
- Use Jenkins environment variables and pipeline capabilities to enhance and customize the pipeline further as needed.

This setup provides a basic continuous integration pipeline using Jenkins and Docker to deploy a simple Python application.