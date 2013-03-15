from fabric.api import env, abort, run
from fabric.contrib.project import rsync_project
from fabric.contrib.console import confirm
from fabric.decorators import runs_once
import os.path

# The user I want to log in with
env.user = 'uw'

# env is an object, so you can append anything else you want to it.
# Here I'm adding a property with the path to my app's directory
# on the server.
env.webapp_path = '/var/www/'

# another custom property, using env.real_fabfile path to set
# the local project dir.
# see http://fabric.readthedocs.org/en/0.9.0/usage/env.html
env.local_project_dir = os.path.dirname(env.real_fabfile)


# My <target> is named production.
def production():
    env.name = 'production'
    env.hosts = [
        'block647048-4cf.blueboxgrid.com',
    ]


#######################

# My rsync command. Makes use of the contributed `rsync_project` command.
def rsync(extras=''):
    """
    Rsync project files
    """
    rsync_project(
        remote_dir=env.webapp_path,
        local_dir="{0}/".format(env.local_project_dir),
        delete=True,
        exclude=env.excluded + ['fabfile.py', '.*', '*.pyc', '*.iml', '*~'],
        extra_opts='--archive --update ' + extras,
    )