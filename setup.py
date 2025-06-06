from setuptools import setup

setup(
    name='abbanner',
    version='0.2',
    description='Custom Terminal Banner by AbhiByte',
    author='AbhiByte',
    author_email='your-email@example.com',
    py_modules=['abbanner'],
    install_requires=['psutil>=5.8.0'],
    entry_points={
        'console_scripts': [
            'abbanner=abbanner:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)