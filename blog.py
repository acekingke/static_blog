#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template,g, request
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from flask.ext.paginate import Pagination

from search import build_index
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
WHOOSH_BASE = './'+FLATPAGES_ROOT+'/'+POST_DIR+'/'
app = Flask(__name__)
app.config.from_object(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)

def get_all():
    if not hasattr(g, 'all'):
        app.logger.debug('has start ')
        g.all = [p for p in flatpages if p.path.startswith(POST_DIR)]    
def get_entry_for_page(page,length,entries):
    entry_page=[]
    for i in range(10):
        index= page*10-10+i
        if index < len(entries):
            entry_page.append(entries[index])
    return entry_page

@app.route('/')
@app.route('/<int:page>')
def index(page = 1):
    """On the index page of our blog, show a list of blog posts"""
    #if has_attribute
    get_all()
    posts = g.all[PER_PAGE*(page - 1):page*PER_PAGE]
    form = SearchForm()
    pagination = Pagination(page=page, bs_version=3,total=len(g.all), per_page=PER_PAGE, record_name='posts')
    return render_template('index.html', form = form, posts=posts, pagination=pagination)

@app.route('/search', methods=['GET', 'POST']) 
def search():
    page=1
    if request.method=='POST':
        entries=[]
        
        keywords = request.form['search'].split(' ')
        # 搜索
        entries = whoosh_search(keywords)        
    else:
        try:
            page=int(request.args.get('page',1))
        except ValueError:
            page=1
    page_entries=get_entry_for_page(page,PER_PAGE,entries)
    get_all()
   
    posts = [p for p in g.all if p.path in [ POST_DIR+'/'+k[0][:-3] for k in page_entries]]    
    pagination=Pagination(page=page, total=len(entries), search=False, record_name='result')
    return render_template('index.html', form = SearchForm(), posts=posts, pagination=pagination)

@app.route('/posts/<name>')
def post(name):
    """For blogpost type pages"""
    path = u'{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)


def whoosh_search(keywords):
    from whoosh.index import create_in,open_dir
    from whoosh.qparser import QueryParser
    indexFile = open_dir('./tmp')
    resultsList = []
    for key in keywords:
        searchQuery = QueryParser("content", indexFile.schema).parse(key)
        
        with indexFile.searcher() as searcher:
            # resultsList.append(searcher.search(searchQuery, limit=1000, terms=True))
            searchResult = searcher.search(searchQuery, limit=1000, terms=True)
            for result in searchResult:
                # resultsList.append(list(result["title"], result["path"]))
                resultsList.append((result["title"], result["path"]))
    return resultsList

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        #freezer.freeze()
        build_index(WHOOSH_BASE)
    elif len(sys.argv) > 1 and sys.argv[1] == "search":
        #freezer.freeze()
        print whoosh_search([u'执行'])
    else:
        
        app.run(host='0.0.0.0', debug=True)