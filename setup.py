from setuptools import setup

setup(
    name="style-profile",
    version="0.2.0",
    packages=["style_profile"],
    package_data={"style_profile": ["*.so"]},
    include_package_data=True,
)
