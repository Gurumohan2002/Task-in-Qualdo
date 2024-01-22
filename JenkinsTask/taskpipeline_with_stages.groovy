pipeline {
    agent any
    stages {
        stage('stage1') {
            when {
                expression { true } 
            }
            steps {
                echo 'Hello World !'
            }
        }

        stage('stage2') {
            when {
                expression { params.stage2 == true }
            }
            steps {
                echo 'Bye Bye !'
            }
        }

        stage('stage3') {
            when {
                expression { params.stage3 == true }
            }
            steps {
                echo 'I am Gurumohan.'
            }
        }
    }

    parameters {
        // booleanParam(name: 'stage1', defaultValue: true, description: 'Run Satge 1')
        // booleanParam(name: 'stage2', defaultValue: false, description: 'Run Stage 2')
        booleanParam(name: 'stage3', defaultValue: true, description: 'Run Stage 3')
    }
}