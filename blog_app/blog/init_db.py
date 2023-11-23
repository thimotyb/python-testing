# python init_db.py
# set FLASK_APP=blog/app.py 
# python -m flask run
if __name__ == "__main__":
    from models import Article
    Article.create_table()