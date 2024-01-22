pipeline {
    agent any
    stages {
        stage('1') {
            steps {
                echo 'Hello World'
            }
        }
        stage('2') {
            steps {
                echo 'I am Gurumohan'
            }
        }
    }
    post {
        success {
            build job: 'Triggered_a_pipeline', wait: false
        }
    }
}
