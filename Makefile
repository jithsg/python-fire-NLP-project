install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	python -m textblob.download_corpora
lint:
	pylint --disable=R,C,W1203,W0703 *.py nlplogic/*.py
format:
	black *.py
test:
	python -m pytest -vv --cov=nlplogic test_corenlp.py
all: install format lint test	