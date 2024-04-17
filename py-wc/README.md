# py-wc

[![PyPI](https://img.shields.io/pypi/v/py-wc.svg)](https://pypi.org/project/py-wc/)
[![Changelog](https://img.shields.io/github/v/release/Ismailtlem/py-wc?include_prereleases&label=changelog)](https://github.com/Ismailtlem/py-wc/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/Ismailtlem/py-wc/blob/master/LICENSE)

python wc tool

## Installation

Install this tool using `pip`:

```bash
pip install py-wc
```

## Usage

For help, run:

```bash
py-wc --help
```

You can also use:

```bash
python -m py_wc --help
```

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

```bash
cd py-wc
python -m venv venv
source venv/bin/activate
```

Now install the dependencies and test dependencies:

```bash
pip install -e '.[test]'
```

To run the tests:

```bash
pytest
```

## Usage

If you have a virtualenv set up, you can just run the cli like the following

```bash
py-wc -p filename [option]
```

The following options are supported:

- `-w`: prints the number of words in the file
- `-l`: prints the number of lines in the file
- `-c`: prints the number of bytes in the file
- `-m`: prints the number of characters in the file

The tool can also be used in stdin mode as follows:

```bash
cat filename | py-wc -p filename [option]
```
