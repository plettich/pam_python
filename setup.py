# -*- coding: utf-8 -*-

from setuptools import setup

#VERSION="2.1dev4"
VERSION = "2.11dev0"

install_requires = [
    'requests>=2.23',
    'passlib>=1.7.2'
]

setup(
    name='privacyidea_pam',
    version=VERSION,
    author='privacyidea.org',
    license='AGPLv3',
    author_email='cornelius@privacyidea.org',
    url='http://www.privacyidea.org',
    keywords='OTP, two factor authentication, management, security',
    py_modules=['privacyidea_pam'],
    install_requires=install_requires,
    classifiers=["Framework :: Flask",
                 "License :: OSI Approved :: "
                 "GNU Affero General Public License v3",
                 "Programming Language :: Python",
                 "Development Status :: 5 - Production/Stable",
                 "Topic :: Internet",
                 "Topic :: Security",
                 "Topic :: System ::"
                 " Systems Administration :: Authentication/Directory"
                 ],
    zip_safe=False
)
