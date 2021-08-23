from setuptools import setup, find_packages

setup(
    name="operations",
    version="0.0.1",
    description="Learning pytest",
    python_requires=">=3.8",
    packages=find_packages(),
    include_package_data=True,
    package_dir={"": "."},
)
