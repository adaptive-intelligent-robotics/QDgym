from setuptools import setup

setup(
    name="QDgym_extended",
    url="https://github.com/adaptive-intelligent-robotics/QDgym_extended.git",
    author="Olle Nilsson, Bryan Lim, Manon Flageat",
    author_email="olle.nilsson19@imperial.ac.uk, bryan.lim16@imperial.ac.uk, manon.flageat18@imperial.ac.uk",
    packages=["QDgym_extended"],
    install_requires=["gym>=0.15.4", "pybullet>=3.0.8", "numpy>=1.19.5"],
    package_data={"QDgym_extended":["assets/*"]},
    version="0.1",
    license="MIT",
    description="QDgym_extended",   
)
