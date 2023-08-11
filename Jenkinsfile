pipeline {
    
    agent any
    
    environment {
        KUBE_CONFIG = credentials('Kubernetes')
        buid_number = "${BUILD_NUMBER}"
    }
    
    stages {
        
        stage("checkout-From-Github") {
            steps {
                echo "clone from github"
                git url:"https://github.com/hacknovas/LearnDjango.git",branch: "main"
            }
        }
        
        stage("Build Image") {
            steps {
                echo "Build emage from dockerfile"
                sh "docker build -t prathameshdoni/test_cicd:${buid_number} ."
            }
        }
        
        stage("Push to Dockerhub"){
            steps{
                withCredentials([usernamePassword(credentialsId:"DockerHub",passwordVariable:"pass1",usernameVariable:"user1")]){
                    echo "pushing to docker hub"
                    sh "docker login -u ${user1} -p ${pass1}"
                    sh "docker push prathameshdoni/test_cicd:${buid_number}"
                }
            }
        }
        
        // stage("Deploy over docker-container") {
        //     steps {
        //         echo "Deploying on container"
        //         sh "docker run -d -p 8000:8000 prathameshdoni/test_cicd:latest"
        //     }
        // }
        
        stage("deploy on k8s"){
            steps {
                script {
                    withCredentials([file(credentialsId: 'Kubernetes', variable: 'KUBE_CONFIG')]) {
                        sh 'cp $KUBE_CONFIG $HOME/.kube/config'
                        sh 'kubectl config use-context minikube' // Set your Kubernetes context
                        sh "sed -i 's/changeHere/test_cicd:${buid_number}/g' deploy.yaml"
                        sh "cat deploy.yaml"
                        sh "kubectl apply -f deploy.yaml"
                        sh "kubectl apply -f service.yaml"
                    }
                }
                
                ///////////////////////////////////////
                // script {
                //     echo "changing image name"
                //     sh "sed -i 's/changeHere/test_cicd:latest/g' deploy.yaml"
                //     sh "cat deploy.yaml"
                //     echo "print 'Deploy.yaml'"
                //     sh "kubectl --kubeconfig=/home/vector/.kube/config create -f deploy.yaml"
                // }
            }
        }
    }
}
