pipeline {
    agent any
    stages {
        stage('1a') {
            steps {
                echo 'Hello World New !'
            }
        }
        stage('2a') {
            steps {
                echo 'Hi I am Gurumohan'
            }
        }
    }
}