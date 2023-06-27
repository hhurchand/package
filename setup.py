import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
with open("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh]

setuptools.setup(
    name="is_number",
    version="0.0.1",
    author="H Hurchand",
    author_email="h.hurchand@gmail.com",
    description="A Python module to determine if something is a number.",
    long_description=long_description,
    long_description_content_type="text/md",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
)