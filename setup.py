from setuptools import setup

setup(
    name="yousign",
    version="0.1",
    description="YouSign python API",
    url="http://github.com/weassur/yousign-python",
    author="Thibaut Fatus",
    author_email="thibaut@weassur.com",
    license="GPL 3.0",
    packages=["yousign"],
    install_requires=["requests"],
    zip_safe=False,
)
