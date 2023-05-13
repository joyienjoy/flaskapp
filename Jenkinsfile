pipeline {
  agent any
  environment {
    DOCKERHUB_CREDENTIALS = credentials('JenkinsLogin')
  }
  stages {
    stage('Git') {
      steps {
        git branch: 'main', changelog: false, poll: false, url: 'https://github.com/joyienjoy/flaskapp.git'
      }
    }
    stage('Build') {
      steps {
        sh 'docker build -t joydeep2022/flaskappsave .'
      }
    }
    stage('Login') {
      steps {
        sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
      }
    }
    stage('Push') {
      steps {
        sh 'docker push joydeep2022/flaskappsave'
        sh 'docker logout'
      }
    }
  }
}
