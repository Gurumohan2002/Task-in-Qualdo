pipeline {
    agent any
    parameters {
        string(name: 'NAME', defaultValue: 'Gurumohan', description: 'Who should I say hello to?')

        text(name: 'ABOUTME', defaultValue: 'I am Working at Saturam', description: 'Enter some information about the person')

        booleanParam(name: 'TOGGLE', defaultValue: true, description: 'Toggle this value')

        choice(name: 'CHOOSE', choices: ['Red', 'Blue', 'Green'], description: 'Pick any color')
        
        password(name: 'PASSWORD', defaultValue: 'Guru', description: 'Enter a password')
    }
    stages {
        stage('Example') {
            steps {
                echo "Hello ${params.NAME}!"

                echo "Biography: ${params.ABOUTME}"
    
                echo "Toggle: ${params.TOGGLE}"

                echo "Choice: ${params.CHOICE}"

                echo "Password: ${params.PASSWORD}"
            }
        }
    }
}