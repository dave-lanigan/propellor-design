import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="propellor_design",
    version="0.0.3",
    author="David Lanigan",
    author_email="dav.lanigan@gmail.com",
    description="A package for designing drone propellers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dave-lanigan/propellor-design",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
