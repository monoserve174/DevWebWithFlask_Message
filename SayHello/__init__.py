from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('SayHello')
app.config.from_pyfile('settings.py')
# 模板優化
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)

from SayHello import views, errors, commands
