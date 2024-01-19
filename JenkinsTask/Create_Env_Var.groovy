pipeline {
    agent any
        stages{
        stage("Env Variables") {
            steps {
                echo "${env.MY_NAME}"
}
}
}}