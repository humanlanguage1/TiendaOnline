node{
    stage('SCM Checkout'){
        git credentialsId: 'a8ed62ed-4e59-410a-afa6-48cdb878dc81', url: 'https://github.com/humanlanguage1/TiendaOnline.git'
    }
    
    // Mark the code build 'stage'
    stage ('Build'){
        
    env.WORKSPACE = pwd()

    sh 'virtualenv --python=python34 venv'
    sh 'source venv/bin/activate'

    sh 'pip install -r requirements.txt'

    env.DJANGO_SETTINGS_MODULE = "demoStore.settings.jenkins"
    }

    // Start the app
    stage ('Test'){
    sh 'python34 manage.py test --keepdb'   
    }
}