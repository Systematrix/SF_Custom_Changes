from setuptools import setup, find_packages
import os

version = '12.6.0'

setup(
    name='sf_custom_changes',
    version=version,
    description='SF Custom App',
    author='Systematrix',
    author_email='info@systematrix.co.in',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
