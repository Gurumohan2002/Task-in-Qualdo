pipeline {
    agent any
    parameters {
        string(name: 'Name', defaultValue: '', description: 'Name')
    }
    stages {
        stage('Print Name') {
            steps {
                script {
                    echo "Received Name : ${params.Name}"
                }
            }
        }
    }
}