**To start flask app:
WINDOWS:
- cd blog_app
- python blog\init_db.py
- set FLASK_APP=blog/app.py 
- python -m flask run

LINUX:
- cd blog_app
- FLASK_APP=blog/app.py
- cd blog
- python init_db.py
- python -m flask run

**From tests/test_article folder**

**To start tests without integration:
- cd blog_app\tests\test_article
- python -m pytest -m "not e2e" -v --disable-warnings

**To start only integration tests (requires starting flask):
- cd blog_app\tests\test_article
- python -m pytest -m e2e -v --disable-warnings

** To perform coverage:
- cd blog_app\tests\test_article
- python -m coverage run -m pytest -m "not e2e" --disable-warnings
- python -m coverage report
- python -m coverage html
- python -m coverage-lcov # to convert in lcov format coverage info for Coverage Gutters (Ctrl+Shift+P: Coverage Gutters - Display Coverage)
