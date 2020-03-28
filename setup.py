from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='satang-pro',
    version='1.0.0',
    description='A Python library for Satang Pro API',
    long_description=readme(),
    long_description_content_type="text/markdown",
    url='https://github.com/sang-sakarin/satang-pro',
    author='sang_sakarin',
    author_email='sang_sakarin@outlook.com',
    license='sang_sakarin',
    scripts=[],
    keywords='satang-pro satang-pro-python',
    packages=['satang_pro'],
    install_requires=['requests'],
)
