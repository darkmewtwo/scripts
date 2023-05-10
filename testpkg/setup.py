import setuptools
setuptools.setup(
    name="testpkg",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    # long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    # project_urls={
    #     "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    # },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: auto",
        "Operating System :: OS Independent",
    ],
    # package_dir={"": "testpkg"},
    packages=setuptools.find_packages(include=["importtest", "toimport"]),
    python_requires=">=3.6",
)