from setuptools import find_packages, setup
import os.path
version = "0.2.0"
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))


def readme():
    with open("README.md") as f:
        long_description = f.read()
    return long_description


setup(
    name="multisafepay",
    version=version,
    license="MIT",
    long_description=readme(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    description="Python wrapper for the MultiSafepay API. The version prior 18/09/2019 is moved to the "
                "'mini-multisafepay' package.",
    author="MultiSafepay",
    author_email="integration@multisafepay.com",
    url="https://github.com/MultiSafepay/multisafepay-python-wrapper",
    keywords=["multisafepay", "wrapper", "payment","gateway","ideal","paypal","creditcard","gift cards",
              "sofort banking"],
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],
)
