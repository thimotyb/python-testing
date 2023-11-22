import os
import tempfile

import pytest

from blog.models import Article


@pytest.fixture(autouse=True)
def database():
    #file_name = str(tempfile.TemporaryFile(dir="tmp"))
    _, file_name = tempfile.mkstemp()
    #file_name = "C:\\tmp\\database.db"
    os.environ["DATABASE_NAME"] = file_name
    Article.create_table(database_name=file_name)
    yield
    try:
        os.unlink(file_name)
    except:
        pass