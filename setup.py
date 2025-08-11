from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

# get version from __version__ variable in thai_utils/__init__.py
# Read version without importing the module
version = "0.0.1"
with open("thai_utils/__init__.py", "r") as f:
    for line in f:
        if line.startswith("__version__"):
            version = line.split("=")[1].strip().strip('"').strip("'")
            break

setup(
    name="thai_utils",
    version=version,
    description="Thai language utilities for Frappe/ERPNext",
    author="Your Name",
    author_email="your@email.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
    dependency_links=[],
    python_requires=">=3.8",
)
