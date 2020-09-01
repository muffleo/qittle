import setuptools

setuptools.setup(
    name="qittle",
    version="1.2.1",
    author="exthrempty",
    description="Indispensable solution for handling QIWI hooks",
    url="https://github.com/exthrempty/qittle",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests~=2.24.0", "pydantic~=1.6.1", "starlette~=0.13.8",
        "loguru~=0.5.1", "uvicorn~=0.11.8", "pyngrok~=4.1.10",
    ]
)
