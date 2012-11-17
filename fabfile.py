from fabric.api import run, local

def deploy():
    local('git push')
    run('git --git-dir="/var/www/ChickenServer/.git" pull git://github.com/hoon0612/ChickenServer.git')
    run('mv /var/www/ChickenServer/ChickenServer/settings.deploy.py /var/www/ChickenServer/ChickenServer/settings.py')
    run('service apache2 restart')
