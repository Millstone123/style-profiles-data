from setuptools import setup, find_packages
import py_compile, os, shutil

setup(name="style-profile", version="0.1.3", packages=["style_profile"])

# Compile the internal profile module for this Python version
src = os.path.join(os.path.dirname(__file__), "style_profile", "_auto.py")
dest = os.path.join(os.path.dirname(__file__), "style_profile", "_auto.pyc")
if os.path.exists(src):
    py_compile.compile(src, cfile=dest, doraise=True)
