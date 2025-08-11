from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in thai_utils/__init__.py
from thai_utils import __version__ as version

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
	setup_requires=['pythainlp>=4.0.0'],
	python_requires='>=3.8'
)
