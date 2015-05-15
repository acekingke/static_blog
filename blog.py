#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template,g
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from flask.ext.paginate import Pagination

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
##################################
import sys

####################################
from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, TextAreaField
from wtforms.validators import Required, Length

class SearchForm(Form):
    search = TextField('search', validators = [Required()])
##################################
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'
PAGE_DIR = 'pages'
FLATPAGES_EXTENSION = '.md'
SITE_NAME = u"aceking静态博客"
SERVER_PORT = 5000
PER_PAGE=4
app = Flask(__name__)
app.config.from_object(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)


@app.route('/')
@app.route('/<int:page>')
def index(page = 1):
    """On the index page of our blog, show a list of blog posts"""
    #if has_attribute
    if not hasattr(g, 'all'):
   		app.logger.debug('has start ')
		g.all = [p for p in flatpages if p.path.startswith(POST_DIR)]
    posts = g.all[PER_PAGE*(page - 1):page*PER_PAGE]
    form = SearchForm()
    pagination = Pagination(page=page, bs_version=3,total=len(g.all), per_page=PER_PAGE, record_name='posts')
  
    return render_template('index.html', form = form, posts=posts, pagination=pagination)

@app.route('/search', methods=['GET', 'POST']) 
def search():
    return 'hello'

@app.route('/posts/<name>')
def post(name):
    """For blogpost type pages"""
    path = u'{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(host='0.0.0.0', debug=True)