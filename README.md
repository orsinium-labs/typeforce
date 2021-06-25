# typeforce

**Typeforce** is a CLI tool that enriches your Python environment with type annotations, empowering [mypy](https://mypy.readthedocs.io/en/stable/).

In particular:

+ Generates `py.typed` for annotated packages.
+ Installs missed stub files and plugins.

## py.typed

[PEP-561](https://www.python.org/dev/peps/pep-0561/) says the following:

> Package maintainers who wish to support type checking of their code MUST add a marker file named py.typed to their package supporting typing.

In practice, many maintainers don't know about this marker. So there are tons of packages that do have type annotations but don't have `py.typed`.

Typeforce checks all installed third-party packages and adds `py.typed` into packages that have type annotations.

## stubs and plugins

One of the breaking changes [mypy 0.900 introduced](http://mypy-lang.blogspot.com/2021/06/mypy-0900-released.html?m=1) is moving out all [stubs](https://mypy.readthedocs.io/en/stable/stubs.html) and plugins for third-party packages out of mypy itself. Now, stub files for every such package should be installed manually.

Typeforce scans all installed third-party packages and installs all needed stub files and plugins if available.

## Installation

```bash
python3 -m pip install --user typeforce
```

## Usage

```bash
python3 -m typeforce --exe python3.9
```
