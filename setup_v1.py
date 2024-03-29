"""
-- Created by Pravesh Budhathoki
-- Treeleaf Technologies Pvt. Ltd.
-- Created on 2024-03-28
"""
from setuptools import setup, find_packages

requirements = []

try:
    with open('requirements_v1.txt') as f:
        requirements = f.read().splitlines()
except IOError as e:
    print(e)

setup(
    name='bigdetection',
    version='1.0',
    description='bigdetection',
    author='Pravesh Kaji Budhathoki',
    author_email='pravesh.budhathoki@treeleaf.ai',
    packages=find_packages(),
    namespace_packages=[],
    package_dir={},
    package_data={'': ['*.py', '*.pyi']},
    install_requires=requirements,
    license='',
    zip_safe=False,
    keywords='treeleaf',
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7'
        'Programming Language :: Python :: 3.8'
        'Programming Language :: Python :: 3.9'
    ],
    test_suite='tests')
