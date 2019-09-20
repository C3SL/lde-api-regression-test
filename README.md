# LDE API Regression Test #

Regression test is a tool for validate existent functionality with each new release of code.

## Table of content ##

 [LDE API Regression Test](#lde-api-regression-test)
 - [Getting Started](#getting-started)
    - [Requirements](#requirements)
    - [Installation](#installation)
 - [Usage](#usage)
    - [Set settings.py](set-settings.py)


## Getting Started

### Requirements

- [Python 3.5+](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/installing/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/installation/)

### Installation

Clone this repository

```
git clone git@gitlab.c3sl.ufpr.br:simcaq/lde-api-regression-test.git
```
Go to this repository
```
cd lde-api-regression-test
```
Create a virtual environment
```
virtualenv -p python3.5 env
```
Activate the virtual environment
```
source env/bin/activate
```
Install dependencies
```
pip install -r requirements.txt
```

## Usage

### Configuring settings.py

Set base url to the running API.
Default route of LDE:
```
BASE_URL="https://simcaq.c3sl.ufpr.br/api/v1/"
```
Local environment route:
```
BASE_URL="localhost:PORT"
```
### Command Instructions

```
usage: manage.py <command> [<args>]

positional arguments:
  command     the command to run

optional arguments:
  -h, --help  show this help message and exit

available commands:
  compare                  Compare multiple or one CSV route
  save                     Save multiple or one CSV route
  -h, --help     show this help message and exit
  --route ROUTE  no description
```

### Saving route

### Compare routes