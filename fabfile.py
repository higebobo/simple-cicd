# -*- mode: python -*- -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv
from fabric.api import (env, run, task, put, cd)
from fabric.contrib.project import rsync_project

path = os.path.join(os.path.dirname(__file__), '.env.fabric')
load_dotenv(path, verbose=True)

env.hosts = ['localhost']


@task
def mock():
    run("echo 'hello'")


def env_base(env_type):
    env.hosts = [os.getenv(f'HOST_{env_type}', 'localhost')]
    env.user = os.getenv(f'USER_{env_type}', 'user')
    env.dir = os.getenv(f'DIR_{env_type}', '/var/tmp')
    env.cmd = os.getenv(f'CMD_{env_type}', 'python')
    env.file = os.getenv(f'ENV_{env_type}', '.env')


@task
def test():
    env_base('TEST')


@task
def stage():
    env_base('STAGE')


@task
def prod():
    env_base('PROD')


@task
def deploy():
    app_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
    local_dir = os.path.dirname(os.path.abspath(__file__))

    rsync_project(
        local_dir=local_dir,
        remote_dir=env.dir,
        exclude=['*.orig', '*.bak', '*~', '.git*', '*.pyc', '__pycache__',
                 'README.md', 'env', '.env*', '.pytest_cache', '.coverage',
                 'fabfile.py', 'requirements.txt', 'log/*.*'],
        delete=True)
    if env.file:
        put(env.file, f'{env.dir}/{app_name}/.env')
    with cd(os.path.join(env.dir, app_name)):
        run(f'{env.cmd} -m app')
