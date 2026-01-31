from setuptools import setup

setup(
    name='subdragon',
    version='1.0.0',
    py_modules=['subdragon'],
    install_requires=[
        'requests',
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'subdragon=subdragon:main',
        ],
    },
    author='0xCr7ck3r',
    description='Subdomain Fuzzing Tool',
)