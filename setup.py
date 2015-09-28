from setuptools import setup, find_packages
import curriculum


def read_file(path):
    with open(path, 'r') as fd:
        return fd.read()

setup(
    name='django-cv',
    version=curriculum.__version__,
    url=curriculum.__url__,
    description=curriculum.__doc__,
    long_description=read_file('README.rst'),
    author=curriculum.__author__,
    author_email=curriculum.__email__,
    license=curriculum.__license__,
    platforms='any',
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.2',
        # 'Programming Language :: Python :: 3.3',
        # 'Programming Language :: Python :: 3.4',
        'Framework :: Django',
    ],
    packages=find_packages(exclude=['tests.runtests.main']),
    include_package_data=True,
    test_suite='tests.runtests.main',
    install_requires=read_file('requirements.txt').splitlines(),
)
