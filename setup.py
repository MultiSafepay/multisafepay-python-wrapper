from setuptools import find_packages, setup
version = "1.0.0"


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name='multisafepay-python-wrapper',
    version=version,
    license='MIT',
    long_description=readme(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    description='Python wrapper for the MultiSafepay API',
    author='MultiSafepay',
    author_email='integration@multisafepay.com',
    url='https://github.com/MultiSafepay/multisafepay-python-wrapper',
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT Licence',
    ],
)
