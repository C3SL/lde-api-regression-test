# LDE API Regression Test #


Regression test is a tool for validate existent functionality with each new release of code.

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

### Set settings.py

Set base url to the running API (local ex.: localhost:PORT):

```
BASE_URL="https://simcaq.c3sl.ufpr.br/api/v1/"
```
Set 