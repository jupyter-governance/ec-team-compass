#!/bin/bash
set -eux
python -m venv .venv
source .venv/bin/activate
pip install -r docs/requirements.txt
cd docs
make dirhtml SPHINXOPTS='-W'
