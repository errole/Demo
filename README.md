# Demo

## Setup

Create and acitavte a virtual environment:

```sh
conda create -n Demo python=3.11

conda activate Demo 
```

Install packages:

```sh
#pip install pytest

pip install -r requirements.txt
```

## Usage

Play a game of rock, paper, scissors:

### play the game on a web app
```sh
FLASK_APP=web_app flask run
```

### play the game using command line
```sh
# only works if this file does not mport from other py files:
python app/rps.py

# if this file imports from other local py files:
python -m app.rps
```

## Tests

Run the tests:

```sh
# find all the tests and run them:
pytest
```