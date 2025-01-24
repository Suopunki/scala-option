from setuptools import find_packages, setup

setup(
    name="optionlib",
    packages=find_packages(include=["optionlib"]),
    version="0.1.0",
    description="Scala like Option type in Python",
    Author="Alex Suopanki",
    install_requires=[],
    setup_requires=["pytest_runner"],
    tests_require=["pytest"],
    test_suite="tests"
)

