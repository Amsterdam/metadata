#!groovy

def tryStep(String message, Closure block, Closure tearDown = null) {
    try {
        block();
    }
    catch (Throwable t) {
        slackSend message: "${env.JOB_NAME}: ${message} failure ${env.BUILD_URL}", channel: '#ci-channel', color: 'danger'

        throw t;
    }
    finally {
        if (tearDown) {
            tearDown();
        }
    }
}


node {

    stage("Checkout") {
        checkout scm
    }

    stage("Build base image") {
        tryStep "build", {
            sh "docker-compose build"
        }
    }

stage('Test') {
    tryStep "test", {
            sh "docker-compose run --rm -u root web python manage.py jenkins"
        }, {
            step([$class: "JUnitResultArchiver", testResults: "reports/junit.xml"])

            sh "docker-compose down"
        }
    }

    stage("Build develop image") {
        tryStep "build", {
            def image = docker.build("build.datapunt.amsterdam.nl:5000/atlas/metadata:${env.BUILD_NUMBER}", "web")
            image.push()
            image.push("acceptance")
        }
    }
}

node {
    stage("Deploy to ACC") {
        tryStep "deployment", {
            build job: 'Subtask_Openstack_Playbook',
                    parameters: [
                            [$class: 'StringParameterValue', name: 'INVENTORY', value: 'acceptance'],
                            [$class: 'StringParameterValue', name: 'PLAYBOOK', value: 'deploy-metadata.yml'],
                    ]
        }
    }
}


stage('Waiting for approval') {
    slackSend channel: '#ci-channel', color: 'warning', message: 'Metadata is waiting for Production Release - please confirm'
    input "Deploy to Production?"
}



node {
    stage('Push production image') {
    tryStep "image tagging", {
        def image = docker.image("build.datapunt.amsterdam.nl:5000/atlas/metadata:${env.BUILD_NUMBER}")
        image.pull()

            image.push("production")
            image.push("latest")
        }
    }
}

node {
    stage("Deploy") {
        tryStep "deployment", {
            build job: 'Subtask_Openstack_Playbook',
                    parameters: [
                            [$class: 'StringParameterValue', name: 'INVENTORY', value: 'production'],
                            [$class: 'StringParameterValue', name: 'PLAYBOOK', value: 'deploy-metadata.yml'],
                    ]
        }
    }
}