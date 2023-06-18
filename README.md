# makemake

### Appendix:

Creating a Python CLI:

#### Setup

Dependencies:
```
> pip3 install virtualenv wheel setuptools
```

Create `virtualenv`:
```
> virtualenv venv
```

Enter `venv`:
```
> source venv/bin/activate
```

Install:
```
> python3 setup.py develop
```

Package:
```
> python3 setup.py sdist bdist_wheel
```

Exit `venv`:
```
> deactivate
```