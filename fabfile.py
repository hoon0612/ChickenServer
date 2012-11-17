from fabric.api import run, local

def deploy():
    local('git push')
    run('cd /var/www/ChickenServer.git/; git pull git://github.com/hoon0612/ChickenServer.git')
    run('rm -rf /var/www/ChickenServer')
    run('cp -R /var/www/ChickenServer.git /var/www/ChickenServer')
    run('mv /var/www/ChickenServer/ChickenServer/settings.deploy.py /var/www/ChickenServer/ChickenServer/settings.py')
    run('printf "yes\\n" | /var/www/ChickenServer/manage.py collectstatic')
    run('chown -R www-data.www-data  /var/www/')
    run('service apache2 restart')
