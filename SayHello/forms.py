from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class HelloForm(FlaskForm):
    name = StringField('名字', validators=[DataRequired(), Length(1, 20)])
    body = TextAreaField('內容', validators=[DataRequired(), Length(1, 200)])
    submit = SubmitField('送出')
