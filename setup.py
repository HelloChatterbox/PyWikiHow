from setuptools import setup

setup(
    name='pywikihow',
    version='0.3',
    packages=['pywikihow'],
    url='https://github.com/JarbasAl/PyWikiHow',
    install_requires=["requests", "bs4"],
    license='MIT',
    author='jarbasai',
    author_email='jarbasai@mailfence.com',
    description='unofficial wikihow python api'
)
