pipeline {
  agent any
  stages {
    stage('pull') {
      steps {
        git(url: 'git@github.com:JohnChain/RTWConfigor.git', branch: 'master')
      }
    }

    stage('build') {
      steps {
        sh '''#!/bin/bash

make'''
      }
    }

  }
}