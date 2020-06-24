from setuptools import setup

setup(
    name='pywikihow',
    version='0.5.5',
    packages=['pywikihow'],
    url='https://github.com/OpenJarbas/PyWikiHow',
    install_requires=["requests", "bs4", "requests-cache"],
    license='MIT',
    author='jarbasai',
    author_email='jarbasai@mailfence.com',
    description='unofficial wikihow python api'
)
