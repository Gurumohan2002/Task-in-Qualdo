pipeline {
    agent any
    stages {
        stage('Create directory') {
            steps {
                script {
                    dir('new_dir2') {
                        echo 'Directory successfully created'
                    }
                }
            }
        }

        stage('Create a Text file') {
            steps {
                script {
                  
                    writeFile file: 'new_dir2/file4.txt', text: ''
                    echo 'Text file created'
                }
            }
        }
          stage('Writing Content to file') {
    steps {
        script {
            
            writeFile file: 'new_dir2/file4.txt', text: 'Hello I am Gurumohan'
            echo 'write content in file '
        }
    }
}

        stage('Printing the file Content') {
            steps {
                script {
                    def printfile = readFile(file: 'new_dir2/file4.txt')
                    echo "File Content: ${printfile}"
                }
            }
        }
    }
}