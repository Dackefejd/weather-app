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

        stage("Run Test") {
            steps {
                
                sh 'python3 test_weather.py'
            }
            post {
                success { echo "========Test executed successfully ========" }
                failure { echo "========Test execution failed========" }
            }
        }
    } 
} 