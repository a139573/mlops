# MLOps project

## Overview
This project implements several data preprocessing functions and provides command-line tools to try them.

## Installation
To clone the repository:
'''bash
git clone git@github.com:a139573/mlops.git
cd mlops
'''
To install the CLI locally:
'''bash
pip install .
'''

## 🧩 Project Structure
The project follows a modular structure similar to the CookieCutter standard.
```
Lab0/
├── pyproject.toml
├── pytest.ini
├── README.md
├── src/
│   ├── preprocessing.py
│   └── cli.py
├── tests/
│   ├── test_logic.py
│   └── test_cli.py
│── uv.lock
```

## Data preprocessing features
- Removal of missing values
- Filling missing values
- Removal of duplicated values
- Normalization of numerical values using the min-max method
- Standardization of numerical values using the z-score method
- Clipping numerical values to a certain range
- Conversion of values to integers
- Logarithmic scale transformation
- Tokenization of text into words, selecting only alphanumeric characters and lowercasing words
- Selection of alphanumerical characters and spaces
- Removal of stop-words from text (it should be lower-cased)
- Flatten a list of lists
- Random shuffling of a list of values

## CLI usage
The format of every command is:
'''bash
cli [GROUP] [COMMAND] [OPTIONS]
'''

### Numeric group

#### Normalize values

Command
'''bash
cli numeric normalize --values 1,2,3,4,5 --new-min 0 --new-max 1
'''

Output:
'''bash
[0.0, 0.25, 0.5, 0.75, 1.0]
'''

#### Standardize values

Command
'''bash
cli numeric standardize --values 1,2,3
'''

Output:
'''bash
[-1.2247, 0, 1.2247]
'''

#### Clip values

Command
'''bash
cli numeric clip --values 1,2,3,4,5 --min-value 2 --max-value 4
'''

Output:
'''bash
[2, 2, 3, 4, 4]
'''

#### Convert strings to integers

Command
'''bash
cli numeric to-int --values 1,a,3
'''

Output:
'''bash
[1, 3]
'''

#### Log transformation

Command
'''bash
cli numeric log --values 1,2,3
'''

Output:
'''bash
'''

## Author

Roberto Aldanondo – Public University of Navarre, Spain