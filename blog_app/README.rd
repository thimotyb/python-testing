**To start flask app:
- cd blog_app
- python blog\init_db.py
- set FLASK_APP=blog/app.py 
- python -m flask run

**From tests/test_article folder**

**To start tests without integration:
- cd blog_app\tests\test_article
- python -m pytest -m "not e2e" -v --disable-warnings

**To start only integration tests (requires starting flask):
- cd blog_app\tests\test_article
- python -m pytest -m e2e -v --disable-warnings

** To perform coverage:
- coverage run -m pytest 
- coverage report
- coverage html
- coverage-lcov # to convert in lcov format coverage info for Coverage Gutters (Ctrl+Shift+P: Coverage Gutters - Display Coverage)
