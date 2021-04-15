# typeforce

[PEP-561](https://www.python.org/dev/peps/pep-0561/) says the following:

> Package maintainers who wish to support type checking of their code MUST add a marker file named py.typed to their package supporting typing.

In practice, many maintainers don't know about this marker. So there are tons of packages that do have type annotations but don't have `py.typed`.

**Typeforce** is a CLI tool that checks all installed third-party packages and adds `py.typed` into packages that have type annotations.

## Installation

```bash
python3 -m pip install --user typeforce
```

## Usage

```bash
python3 -m typeforce --exe python3.9
```
