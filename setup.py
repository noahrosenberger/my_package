from setuptools import setup, find_packages

setup(
    name='your_package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # Add your package dependencies here
    ],
    python_requires='>=3.6',
    author='Your Name',
    author_email='your_email@example.com',
    description='A brief description of your package.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/your_package',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)