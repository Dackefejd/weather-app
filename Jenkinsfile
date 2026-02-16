pipeline {
    agent any
    stages {
        stage("Checkout") {
            steps {
                echo "======== Getting code from Github ========"
            }
            post {
                success { echo "======== Checkout was successful ========" }
                failure { echo "======== Checkout failed ========" }
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "======== Creating venv and installing python libs ========"
                sh '''
                    # Create a virtual environment in the workspace 
                        python3 -m venv venv
                    
                    # Update pip and install from your requirements.txt
                    ./venv/bin/python3 -m pip install --upgrade pip
                    ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage("Run pytest") {
            steps {
                echo "======== Run tests with pytest ========"
                sh 'PYTHONPATH=. ./venv/bin/pytest'
            }
            post {
                success { echo "======== The tests passed! ========" }
                failure { echo "======== The tests failed ========" }
            }
        }
    }
    post {
        always {
            echo "======== The pipeline is completed ========"
        }
    }
}