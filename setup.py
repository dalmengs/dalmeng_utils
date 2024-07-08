from setuptools import setup, find_packages

setup(
    name='DalmengUtils',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "aiohttp==3.9.5",
        "python-dotenv==1.0.1"
    ],
    author='dalmeng',
    author_email='dalmengs@naver.com',
    description='Project Utils',
    url='https://github.com/dalmengs/dalmeng_utils',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)
