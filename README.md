[![Build Status](https://travis-ci.org/pdericson/mate.svg?branch=master)](https://travis-ci.org/pdericson/mate)

# Mate

Aye Aye, Captain!

## Use Case 1

```
cat > test.yaml <<EOF
kind: Pod
EOF
./mate test.yaml
test.yaml: u'containers' is a required property

Failed validating u'required' in schema: ...
```

## Getting Started

Python 2:

```
curl -fLo mate https://github.com/pdericson/mate/releases/download/0.1.1/mate-2.7.pex
chmod +x mate
./mate --version
```

Python 3:

```
curl -fLo mate https://github.com/pdericson/mate/releases/download/0.1.1/mate-3.5.pex
chmod +x mate
./mate --version
```

## Development

```
virtualenv .venv
. .venv/bin/activate
pip install -r requirements.txt
python -m mate --version
deactivate
```
