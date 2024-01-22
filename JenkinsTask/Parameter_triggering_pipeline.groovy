pipeline {
    agent any
    
    stages {
        stage('First') {
            steps {

                echo 'Hi Everyone !'
            }
        }
        
        stage('Second') {
            steps {
                 echo 'Hello !'
            }
        }
    }

    post {
        success {

            build( job: 'Parameter_Triggered_pipeline', parameters:[
                string(name: 'Name', value: "Guru")] , wait: false)
        }
    }
}

