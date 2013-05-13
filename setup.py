import os
from setuptools import setup, find_packages

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

setup(name='wercker-getting-started-python',
    version='1.0',
    author='wercker',
    author_email='pleasemailus@wercker.com',
    url='https://github.com/wercker/getting-started-python/',
    packages=find_packages(),
    include_package_data=True,
    description='Example Python app for wercker.com and OpenShift',
    install_requires=open('%s/requirements.txt' % os.environ.get('OPENSHIFT_REPO_DIR', PROJECT_ROOT)).readlines(),
)