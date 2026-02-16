pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo "======== Hämtar kod från Github ========"
                
            }
        }

        stage('Python Tests') {
            agent {
                docker { 
                    image 'python:3.11-slim'
                    
                }
            }
            stages {
                stage('Install and Run') {
                    steps {
                        echo "======== Körs inuti en Python-container ========"
                        sh '''
                            pip install --upgrade pip
                            pip install -r requirements.txt
                            PYTHONPATH=. pytest
                        '''
                    }
                    post {
                        success {
                            echo "======== Alla tester gick igenom i containern! ========"
                        }
                    }
                }
            }
        }
    }
    post {
        always {
            echo "======== Pipelinen är färdig ========"
        }
    }
}