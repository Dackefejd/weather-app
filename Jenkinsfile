pipeline {
    agent any
    stages {
        stage("Checkout") {
            steps {
                echo "========Getting code from Github========"
            }
            post {
                success { echo "========Checkout executed successfully========" }
                failure { echo "========Checkout execution failed========" }
            }
        }
        stage('Install Dependencies') {
    steps {
        echo "======== Installing libraries ========"
        sh 'python3 -m pip install -r requirements.txt'
    }
}
        stage("Run pytest") {
            steps {
                
                sh 'PYTHONPATH=. pytest'
            }
            post {
                success { echo "========Test executed successfully ========" }
                failure { echo "========Test execution failed========" }
            }
        }
    } 
} 