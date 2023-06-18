from setuptools import setup, find_packages

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read()

setup(
    name = 'makemake',
    version = '0.0.1',
    author = 'Drew Malin',
    author_email='drewmalin@gmail.com',
    python_requires ='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independend",
    ],
    entry_points = '''
        [console_scripts]
        makemake=makemake:cli
    '''
)