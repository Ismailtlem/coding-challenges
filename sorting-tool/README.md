# sorting-tool

[![PyPI](https://img.shields.io/pypi/v/sorting-tool.svg)](https://pypi.org/project/sorting-tool/)
[![Changelog](https://img.shields.io/github/v/release/Ismailtlem/sorting-tool?include_prereleases&label=changelog)](https://github.com/Ismailtlem/sorting-tool/releases)
[![Tests](https://github.com/Ismailtlem/sorting-tool/actions/workflows/test.yml/badge.svg)](https://github.com/Ismailtlem/sorting-tool/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/Ismailtlem/sorting-tool/blob/master/LICENSE)

sorting-tool like the unix sort tool

## Installation

Install this tool using `pip`:
```bash
pip install sorting-tool
```
## Usage

For help, run:
```bash
sorting-tool --help
```
You can also use:
```bash
python -m sorting_tool --help
```
## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:
```bash
cd sorting-tool
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
