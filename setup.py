from setuptools import setup, find_packages

setup(
    name='simple_calculator',
    version='1.0',
    packages=find_packages(),
    py_modules = ['calculator'],
    description='A simple calculator class with basic arithmetic operations',
    author='Your Name',
    author_email='your@email.com',
    url='https://github.com/your_username/simple_calculator',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9.13',
    ],
)
