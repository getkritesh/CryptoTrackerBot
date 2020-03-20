# TrackerBot - check cryptocurrencies prices on telegram

import setuptools


setuptools.setup(

    name="trackerbot",
    version="1",

    author="Kritesh Tripathi",
    author_email="tripathi.kritesh@gmail.com",

    install_requires=[
        "python-telegram-bot",
        "requests",
        "matplotlib<2.2.0",
        "image"
    ],

    packages=[
        "cryptotrackerbot",
    ],

    entry_points={
        "console_scripts": [
            "cryptotrackerbot = cryptotrackerbot.__main__:main",
        ],
    },

    include_package_data=True,
    zip_safe=False,

    classifiers=[
        "Not on PyPI"
    ],

)
