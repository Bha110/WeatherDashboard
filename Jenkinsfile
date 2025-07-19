pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'bhakti20/weather-tracker'  // Your DockerHub repo
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    withDockerRegistry([credentialsId: 'dockerhub', url: 'https://index.docker.io/v1/']) {
                        docker.image("${DOCKER_IMAGE}").push("latest")
                    }
                }
            }
        }
    }

    post {
        success {
            echo '✅ Docker image built and pushed successfully to DockerHub!'
        }
        failure {
            echo '❌ Pipeline failed. Check the logs for more info.'
        }
    }
}
